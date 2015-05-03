# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='title',
            new_name='name',
        ),
    ]
