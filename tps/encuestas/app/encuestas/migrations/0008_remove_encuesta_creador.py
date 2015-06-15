# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0007_auto_20150608_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='creador',
        ),
    ]
