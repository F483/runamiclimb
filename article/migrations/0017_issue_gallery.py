# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0006_auto_20141028_2005'),
        ('article', '0016_issue_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='gallery',
            field=models.ForeignKey(related_name='issues', blank=True, to='photologue.Gallery', null=True),
            preserve_default=True,
        ),
    ]
