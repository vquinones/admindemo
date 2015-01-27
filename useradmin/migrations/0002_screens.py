# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Screen',
                'verbose_name_plural': 'Screens',
            },
            bases=(models.Model,),
        ),
    ]
