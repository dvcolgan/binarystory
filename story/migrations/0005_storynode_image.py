# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20150720_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='storynode',
            name='image',
            field=models.ImageField(upload_to=b'story-images', blank=True),
        ),
    ]
