# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_issue_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='ordering_category',
        ),
    ]
