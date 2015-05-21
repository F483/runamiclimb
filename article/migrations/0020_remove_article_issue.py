# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_remove_article_ordering_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='issue',
        ),
    ]
