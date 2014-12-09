# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20141209_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='coverletter',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]
