# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '__first__'),
        ('article', '0012_auto_20141229_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(related_name='article_comments', null=True, to='comment.Comment', blank=True),
            preserve_default=True,
        ),
    ]
