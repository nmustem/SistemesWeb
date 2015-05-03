# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('dni', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=60)),
                ('main_actor', models.CharField(max_length=60)),
                ('director', models.ForeignKey(to='ejemplo.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('title', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('code', models.ForeignKey(to='ejemplo.Film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(to='ejemplo.Genre'),
        ),
    ]
