# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainRouting', '0002_auto_20141004_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='city_name',
            field=models.ForeignKey(verbose_name='city', to='trainRouting.City'),
        ),
    ]
