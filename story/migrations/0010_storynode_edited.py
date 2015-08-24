# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0009_auto_20150820_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='storynode',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]
