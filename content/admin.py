from django.contrib import admin
from django.conf import settings
from .models import *


class BaseModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': [settings.STATIC_URL + 'displays/css/admin.css']
        }


class ImageAdmin(BaseModelAdmin):
    fields = ('title', 'image')
    list_display = ('title', 'image_thumbnail', 'last_modified')


class VideoAdmin(BaseModelAdmin):
    fields = ('title', 'duration', 'override_color', 'has_alpha', 'video')
    list_display = ('title', 'duration', 'has_alpha', 'last_modified')


class SponsorAdmin(BaseModelAdmin):
    fields = ('name', 'type', 'image')
    list_display = ('name', 'image_thumbnail', 'type', 'last_modified')
    list_filter = ('type',)
    ordering = ['name']


class SponsorTypeAdmin(BaseModelAdmin):
    fields = ('name', )
    list_display = ('name',)
    ordering = ['name']

class HashtagAdmin(BaseModelAdmin):
    list_display = ('name', 'last_modified')


class SocialItemAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__first_name', 'user__last_name',
                     'text', 'media_caption', 'hashtags__name']
    fields = ('original_id', 'channel', 'state', 'user', 'text', 'media_type',
              'media_caption', 'image', 'video', 'hashtags', 'likes', 'shares')
    list_display = ('text', 'channel', 'media_type', 'get_media', 'user',
                    'user_profile_image', 'state', 'created_at')
    list_filter = ('state', 'channel')
    list_editable = ('state',)
    list_per_page = 50
    ordering = ['-created_at']


class SocialUserAdmin(admin.ModelAdmin):
    fields = ('original_id', 'username', 'first_name', 'last_name', 'image')
    list_display = ('username', 'first_name', 'last_name', 'last_modified')


class WordCloudTermAdmin(admin.ModelAdmin):
    fields = ('term', 'weight')
    list_display = ('term', 'weight', 'last_modified')


class DemographicAdmin(admin.ModelAdmin):
    fields = ('label', 'count', 'type')
    list_display = ('label', 'count', 'type', 'last_modified')


class InfluencerAdmin(admin.ModelAdmin):
    fields = ('handle', 'score', 'image')
    list_display = ('handle', 'score', 'image_thumbnail', 'last_modified')


admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorType, SponsorTypeAdmin)
admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(SocialItem, SocialItemAdmin)
admin.site.register(SocialUser, SocialUserAdmin)
admin.site.register(WordCloudTerm, WordCloudTermAdmin)
admin.site.register(Demographic, DemographicAdmin)
admin.site.register(Influencer, InfluencerAdmin)

