# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0006_remove_respuesta_finalizada'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='finalizada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='usuario',
            field=models.ForeignKey(related_name='respuestas', default=1, to='encuestas.User'),
            preserve_default=False,
        ),
    ]
