# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0004_encuesta_fecha_expiracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finalizada', models.BooleanField(default=False)),
                ('encuesta', models.ForeignKey(related_name='respuestas', to='encuestas.Encuesta')),
                ('opcion', models.ForeignKey(related_name='respuestas', to='encuestas.Opcion')),
            ],
        ),
    ]
