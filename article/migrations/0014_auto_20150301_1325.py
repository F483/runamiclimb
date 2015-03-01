# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_article_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='blog_article',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='blog_date',
            field=models.DateField(default=None, null=True),
            preserve_default=True,
        ),
    ]
