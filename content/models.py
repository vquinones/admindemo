from django.db import models
from django.conf import settings
from django.utils import timezone
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

saved_file.connect(generate_aliases_global)

SOCIAL_CHANNELS = (
    ('chatter', 'Chatter'),
    ('instagram', 'Instagram'),
    ('twitter', 'Twitter'),
)


class BaseModel(models.Model):
    """
    Abstract model that defines a Display.
    """
    last_modified = models.DateTimeField(auto_now=True,
                                         default=timezone.now)
    created = models.DateTimeField(auto_now_add=True,
                                   default=timezone.now)

    last_modified.db_index = True
    created.db_index = True

    ordering = ('-last_modified',)

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    image = ThumbnailerImageField(upload_to='uploads/images')

    class Meta:
        abstract = True

    def image_absolute_url(self, alias='original'):
        if self.image:
            if alias == 'original':
                url = self.image.url
            else:
                url = get_thumbnailer(self.image)[alias].url
            return settings.BASE_IMAGE_URL + url
        else:
            return None

    def large_image_thumbnail(self):
        if self.image:
            url = settings.BASE_IMAGE_URL +\
                get_thumbnailer(self.image)['large_thumbnail'].url
            return '<img src="%s" />' % url
        else:
            return None

    large_image_thumbnail.allow_tags = True
    large_image_thumbnail.short_description = "Image"

    def image_thumbnail(self):
        if self.image:
            url = settings.BASE_IMAGE_URL +\
                get_thumbnailer(self.image)['thumbnail'].url
            return '<img src="%s" />' % url
        else:
            return None

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Thumbnail"


class VideoMixin(models.Model):
    video = models.FileField(upload_to='uploads/videos', null=True,
                             blank=True)

    class Meta:
        abstract = True

    def video_absolute_url(self):
        if self.video:
            return settings.BASE_IMAGE_URL + self.video.url
        else:
            return None

    video_absolute_url.allow_tags = True
    video_absolute_url.short_description = "Video URL"


class Hashtag(BaseModel):
    name = models.CharField(unique=True, max_length=255)
    name.db_index = True

    def __unicode__(self):
        return self.name


class Image(BaseModel, ImageMixin):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class WordCloudTerm(BaseModel):
    """
    Radian6 word cloud data
    """
    term = models.CharField(max_length=255)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.term


class Demographic(BaseModel):
    """
    Radian6 demographic data
    """
    label = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class Influencer(BaseModel, ImageMixin):
    """
    Radian6 influencer data
    """
    handle = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.handle


class SocialUser(BaseModel, ImageMixin):
    original_id = models.CharField(max_length=255)
    channel = models.CharField(max_length=255, choices=SOCIAL_CHANNELS)
    username = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    # Indexes
    original_id.db_index = True

    class Meta:
        unique_together = ('original_id', 'channel',)

    def __unicode__(self):
        if self.username:
            return self.username
        else:
            return self.first_name + ' ' + self.last_name


class SocialItem(BaseModel, ImageMixin, VideoMixin):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    ITEM_STATES = (
        (0, 'Unpublished'),
        (1, 'Deleted'),
        (2, 'Published')
    )

    original_id = models.CharField(max_length=255)
    channel = models.CharField(max_length=255, choices=SOCIAL_CHANNELS)
    state = models.SmallIntegerField(choices=ITEM_STATES, default=0)
    user = models.ForeignKey(SocialUser, related_name='social_item_user')
    text = models.TextField(blank=True)
    media_type = models.CharField(max_length=255, choices=MEDIA_TYPES,
                                  blank=True)
    media_caption = models.TextField(blank=True)
    hashtags = models.ManyToManyField(Hashtag, null=True,
                                      related_name='social_item_hashtag')
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    created_at = models.DateTimeField()

    # Indexes
    original_id.db_index = True
    channel.db_index = True

    class Meta:
        unique_together = ('original_id', 'channel',)

    def get_media(self):
        if self.media_type == 'image':
            if self.image:
                url = settings.BASE_IMAGE_URL +\
                    get_thumbnailer(self.image)['large_thumbnail'].url
                return '<img src="%s" />' % url
            else:
                return ''
        else:
            if self.video:
                url = settings.BASE_IMAGE_URL + self.video.url
                return '<video width="200" height="200" src="%s" autoplay loop />' % url
            else:
                return ''

    get_media.allow_tags = True
    get_media.short_description = "Media"

    def user_profile_image(self):
        if self.user.image:
            url = settings.BASE_IMAGE_URL +\
                get_thumbnailer(self.user.image)['thumbnail'].url
            return '<img src="%s" />' % url
        else:
            return None

    user_profile_image.allow_tags = True
    user_profile_image.short_description = "Profile Image"


class SponsorType(BaseModel):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Sponsor(BaseModel, ImageMixin):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(SponsorType, related_name='sponsor_type')

    def __unicode__(self):
        return self.name


class Video(BaseModel, VideoMixin):
    COLORS = (
        ('009DDC', 'Blue'),
        ('959595', 'Gray'),
        ('B5D334', 'Green'),
        ('E98300', 'Orange'),
        ('3FCFD5', 'Teal'),
        ('FECB00', 'Yellow'),
    )

    title = models.CharField(max_length=255)
    override_color = models.CharField(max_length=6, choices=COLORS,
                                      default='', null=True, blank=True)
    duration = models.FloatField(default=15, blank=True, null=True)
    has_alpha = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
