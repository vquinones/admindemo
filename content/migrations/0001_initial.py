# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('label', models.CharField(max_length=255)),
                ('count', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('name', models.CharField(unique=True, max_length=255, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/images')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/images')),
                ('handle', models.CharField(max_length=255)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/images')),
                ('video', models.FileField(null=True, upload_to=b'uploads/videos', blank=True)),
                ('original_id', models.CharField(max_length=255, db_index=True)),
                ('channel', models.CharField(db_index=True, max_length=255, choices=[(b'chatter', b'Chatter'), (b'instagram', b'Instagram'), (b'twitter', b'Twitter')])),
                ('state', models.SmallIntegerField(default=0, choices=[(0, b'Unpublished'), (1, b'Deleted'), (2, b'Published')])),
                ('text', models.TextField(blank=True)),
                ('media_type', models.CharField(blank=True, max_length=255, choices=[(b'image', b'Image'), (b'video', b'Video')])),
                ('media_caption', models.TextField(blank=True)),
                ('likes', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField()),
                ('hashtags', models.ManyToManyField(related_name='social_item_hashtag', null=True, to='content.Hashtag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/images')),
                ('original_id', models.CharField(max_length=255, db_index=True)),
                ('channel', models.CharField(max_length=255, choices=[(b'chatter', b'Chatter'), (b'instagram', b'Instagram'), (b'twitter', b'Twitter')])),
                ('username', models.CharField(max_length=255, blank=True)),
                ('first_name', models.CharField(max_length=255, blank=True)),
                ('last_name', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/images')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SponsorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('video', models.FileField(null=True, upload_to=b'uploads/videos', blank=True)),
                ('title', models.CharField(max_length=255)),
                ('override_color', models.CharField(default=b'', max_length=6, null=True, blank=True, choices=[(b'009DDC', b'Blue'), (b'959595', b'Gray'), (b'B5D334', b'Green'), (b'E98300', b'Orange'), (b'3FCFD5', b'Teal'), (b'FECB00', b'Yellow')])),
                ('duration', models.FloatField(default=15, null=True, blank=True)),
                ('has_alpha', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WordCloudTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True, db_index=True)),
                ('term', models.CharField(max_length=255)),
                ('weight', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='type',
            field=models.ForeignKey(related_name='sponsor_type', to='content.SponsorType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='socialuser',
            unique_together=set([('original_id', 'channel')]),
        ),
        migrations.AddField(
            model_name='socialitem',
            name='user',
            field=models.ForeignKey(related_name='social_item_user', to='content.SocialUser'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='socialitem',
            unique_together=set([('original_id', 'channel')]),
        ),
    ]
