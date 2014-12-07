# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(related_name='articles', to='article.Issue', null=True),
            preserve_default=True,
        ),
    ]
