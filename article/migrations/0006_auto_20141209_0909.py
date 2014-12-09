# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_issue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-year', '-month']},
        ),
        migrations.AddField(
            model_name='article',
            name='email',
            field=models.EmailField(default=datetime.date(2014, 12, 9), max_length=1024),
            preserve_default=False,
        ),
    ]
