# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainRouting', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cities',
            new_name='City',
        ),
        migrations.RenameModel(
            old_name='Stations',
            new_name='Station',
        ),
    ]
