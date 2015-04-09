# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def set_poll_results_privacy_type(apps, schema_editor):

    Topic = apps.get_model("pybb", "Topic")
    Topic.objects.exclude(poll_type=0) \
                 .update(poll_result_privacy=0)

class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0002_auto_20150409_0915'),
    ]

    operations = [
        migrations.RunPython(set_poll_results_privacy_type),
    ]
