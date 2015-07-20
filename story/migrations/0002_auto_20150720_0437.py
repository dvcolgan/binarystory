# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storynode',
            name='choice_a_label',
            field=models.CharField(default='choice a', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storynode',
            name='choice_b_label',
            field=models.CharField(default='choice b', max_length=255),
            preserve_default=False,
        ),
    ]
