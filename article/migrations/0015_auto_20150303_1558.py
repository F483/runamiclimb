# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20150301_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blog_date',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(related_name='articles', blank=True, to='article.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(related_name='articles', blank=True, to='article.Issue', null=True),
            preserve_default=True,
        ),
    ]
