# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_auto_20150720_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storynode',
            name='voiceover',
        ),
        migrations.AddField(
            model_name='storynode',
            name='voiceover_mp3',
            field=models.FileField(upload_to=b'client/assets/story-voiceovers-mp3', blank=True),
        ),
        migrations.AddField(
            model_name='storynode',
            name='voiceover_ogg',
            field=models.FileField(upload_to=b'client/assets/story-voiceovers-ogg', blank=True),
        ),
    ]
