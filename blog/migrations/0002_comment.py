# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.CharField(max_length=140)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]