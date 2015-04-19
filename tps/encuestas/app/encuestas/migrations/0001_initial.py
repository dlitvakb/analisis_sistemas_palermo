# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, unique=True)),
                ('visitado', models.BooleanField(default=False)),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=255)),
                ('grupo', models.ForeignKey(to='encuestas.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(unique=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(to='encuestas.Pregunta'),
        ),
        migrations.AddField(
            model_name='link',
            name='user',
            field=models.ForeignKey(to='encuestas.User'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='creador',
            field=models.ForeignKey(to='encuestas.User'),
        ),
    ]
