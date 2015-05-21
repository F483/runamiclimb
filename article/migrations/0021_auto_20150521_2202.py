# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_remove_article_issue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Article',
            old_name='blog_date',
            new_name='date'
        ),
        migrations.RenameField(
            model_name='Article',
            old_name='blog_article',
            new_name='blog'
        ),
    ]
