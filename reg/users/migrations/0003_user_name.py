# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_last_login_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
