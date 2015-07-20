# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_auto_20150720_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storynode',
            name='voiceover',
            field=models.FileField(upload_to=b'client/assets/story-voiceovers', blank=True),
        ),
    ]
