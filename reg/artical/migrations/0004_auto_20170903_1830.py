# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0003_auto_20170903_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paper',
            options={'verbose_name': '论文', 'verbose_name_plural': '论文'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': '审稿', 'verbose_name_plural': '审稿'},
        ),
    ]
