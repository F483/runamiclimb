# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_remove_article_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ordering_category',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='ordering_featured',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='gallery',
            field=models.ForeignKey(related_name='articles', blank=True, to='photologue.Gallery', null=True),
            preserve_default=True,
        ),
    ]
