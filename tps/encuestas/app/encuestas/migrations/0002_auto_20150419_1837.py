# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='usuarios',
            field=models.ManyToManyField(related_name='encuestas_participadas', to='encuestas.User'),
        ),
        migrations.AddField(
            model_name='link',
            name='enviado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='creador',
            field=models.ForeignKey(related_name='encuestas', to='encuestas.User'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='encuesta',
            field=models.ForeignKey(related_name='grupos', to='encuestas.Encuesta'),
        ),
        migrations.AlterField(
            model_name='link',
            name='encuesta',
            field=models.ForeignKey(related_name='links', to='encuestas.Encuesta'),
        ),
        migrations.AlterField(
            model_name='link',
            name='user',
            field=models.ForeignKey(related_name='links', to='encuestas.User'),
        ),
        migrations.AlterField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(related_name='opciones', to='encuestas.Pregunta'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='grupo',
            field=models.ForeignKey(related_name='preguntas', to='encuestas.Grupo'),
        ),
    ]
