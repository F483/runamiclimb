# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20141207_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
