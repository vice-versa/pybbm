# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='poll_result_privacy',
            field=models.IntegerField(default=0, verbose_name='Poll results privacy', choices=[(0, 'Public poll result'), (1, 'Private poll result')]),
            preserve_default=True,
        ),
    ]
