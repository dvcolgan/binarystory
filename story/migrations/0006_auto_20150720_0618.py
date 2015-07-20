# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audiofield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_storynode_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='storynode',
            name='voiceover',
            field=audiofield.fields.AudioField(help_text=b'Allowed type - .mp3, .wav, .ogg', upload_to=b'client/assets/story-voiceovers', blank=True),
        ),
        migrations.AlterField(
            model_name='storynode',
            name='image',
            field=models.ImageField(upload_to=b'client/assets/story-images/', blank=True),
        ),
    ]
