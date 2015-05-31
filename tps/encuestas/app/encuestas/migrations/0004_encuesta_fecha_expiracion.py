# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0003_encuesta_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='fecha_expiracion',
            field=models.DateTimeField(null=True),
        ),
    ]
