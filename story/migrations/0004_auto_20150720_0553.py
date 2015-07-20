# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20150720_0440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storynode',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='storynode',
            name='title',
            field=models.CharField(default='Title', max_length=255),
            preserve_default=False,
        ),
    ]
