# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20150303_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='pdf',
            field=models.FileField(default=None, null=True, upload_to=b'issues'),
            preserve_default=True,
        ),
    ]
