# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_remove_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
