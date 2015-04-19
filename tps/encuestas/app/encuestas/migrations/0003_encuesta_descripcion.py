# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_auto_20150419_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='descripcion',
            field=models.TextField(default=b''),
        ),
    ]
