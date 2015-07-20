# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoryNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('choice_a', models.OneToOneField(related_name='parent_a', to='story.StoryNode')),
                ('choice_b', models.OneToOneField(related_name='parent_b', to='story.StoryNode')),
            ],
        ),
    ]
