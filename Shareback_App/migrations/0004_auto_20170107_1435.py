# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shareback_App', '0003_auto_20161230_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='rating_1',
            field=models.IntegerField(db_column='rating_1', default=0),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='rating_2',
            field=models.IntegerField(db_column='rating_2', default=0),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='rating_3',
            field=models.IntegerField(db_column='rating_3', default=0),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='rating_4',
            field=models.IntegerField(db_column='rating_4', default=0),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='rating_5',
            field=models.IntegerField(db_column='rating_5', default=0),
        ),
    ]
