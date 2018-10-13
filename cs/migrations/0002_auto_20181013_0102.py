# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finalyearstudents',
            old_name='customer',
            new_name='studentmail',
        ),
        migrations.AlterField(
            model_name='finalyearstudents',
            name='priority',
            field=models.IntegerField(choices=[(0, 'I year'), (1, 'II year'), (2, 'III year')], default=1),
        ),
    ]
