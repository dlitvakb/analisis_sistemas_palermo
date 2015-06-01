# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0005_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='finalizada',
        ),
    ]
