# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('power', models.DecimalField(decimal_places=2, max_digits=4)),
                ('producer_id_hash', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('prizes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beers.Producer'),
        ),
        migrations.AddField(
            model_name='bar',
            name='beers',
            field=models.ManyToManyField(to='beers.Beer'),
        ),
    ]