# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'feedbacks',
            },
        ),
        migrations.CreateModel(
            name='SessionFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'session_files',
            },
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('session_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('session_name', models.CharField(max_length=120)),
                ('timestamp', models.DateField(auto_now=True)),
                ('rating_1', models.IntegerField()),
                ('rating_2', models.IntegerField()),
                ('rating_3', models.IntegerField()),
                ('rating_4', models.IntegerField()),
                ('rating_5', models.IntegerField()),
            ],
            options={
                'db_table': 'sessions',
            },
        ),
        migrations.AddField(
            model_name='sessionfiles',
            name='session_id',
            field=models.ForeignKey(db_column='session_id', on_delete=django.db.models.deletion.CASCADE, to='Shareback_App.Sessions'),
        ),
        migrations.AddField(
            model_name='feedbacks',
            name='session_id',
            field=models.ForeignKey(db_column='session_id', on_delete=django.db.models.deletion.CASCADE, to='Shareback_App.Sessions'),
        ),
    ]
