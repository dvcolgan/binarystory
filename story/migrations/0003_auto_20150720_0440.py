# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20150720_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storynode',
            name='choice_a',
            field=models.OneToOneField(related_name='parent_a', null=True, blank=True, to='story.StoryNode'),
        ),
        migrations.AlterField(
            model_name='storynode',
            name='choice_b',
            field=models.OneToOneField(related_name='parent_b', null=True, blank=True, to='story.StoryNode'),
        ),
    ]
