# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0006_auto_20141028_2005'),
        ('article', '0009_issue_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='gallery',
            field=models.ForeignKey(related_name='articles', to='photologue.Gallery', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ForeignKey(related_name='articles', to='photologue.Photo', null=True),
            preserve_default=True,
        ),
    ]
