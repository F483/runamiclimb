# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_remove_article_ordering_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='ordering_featured',
        ),
    ]
