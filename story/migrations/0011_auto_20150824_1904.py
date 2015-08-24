# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0010_storynode_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storynode',
            name='choice_a',
            field=models.ForeignKey(related_name='parent_a', blank=True, to='story.StoryNode', null=True),
        ),
        migrations.AlterField(
            model_name='storynode',
            name='choice_b',
            field=models.ForeignKey(related_name='parent_b', blank=True, to='story.StoryNode', null=True),
        ),
    ]
