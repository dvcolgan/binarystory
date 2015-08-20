# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0008_auto_20150720_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storynode',
            name='choice_a_label',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='storynode',
            name='choice_b_label',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
