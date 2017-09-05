# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=30, verbose_name='作者名称')),
                ('authorWorkplace', models.CharField(max_length=30, verbose_name='作者工作单位')),
                ('authorAdress', models.CharField(max_length=30, verbose_name='作者地址')),
                ('authorPhone', models.CharField(max_length=30, verbose_name='作者联系方式')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentName', models.CharField(max_length=30, verbose_name='评论人')),
                ('commentTime', models.DateField(verbose_name='评论时间')),
                ('commentLevel', models.CharField(max_length=30, verbose_name='评论等级')),
                ('commentReviewer', models.CharField(max_length=30, verbose_name='审核人')),
                ('commentReviewTime', models.DateField(verbose_name='审核时间')),
                ('commentStatus', models.CharField(max_length=30, verbose_name='审核状态')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='inspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspectTime', models.DateField(verbose_name='审稿时间')),
                ('inspectIdea', models.CharField(max_length=30, verbose_name='审稿意见')),
                ('inspectResult', models.CharField(max_length=30, verbose_name='审稿结果')),
            ],
        ),
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jourName', models.CharField(max_length=30, verbose_name='期刊名称')),
                ('jourLevel', models.CharField(max_length=30, verbose_name='期刊等级')),
                ('jourManager', models.CharField(max_length=30, verbose_name='期刊联系人')),
                ('jourPhone', models.CharField(max_length=30, verbose_name='期刊联系电话')),
                ('jourUrl', models.CharField(max_length=50, verbose_name='期刊网址')),
            ],
            options={
                'verbose_name': '期刊',
                'verbose_name_plural': '期刊',
            },
        ),
        migrations.CreateModel(
            name='paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paperChineseName', models.CharField(max_length=30, verbose_name='论文中文名称')),
                ('paperEnglishName', models.CharField(max_length=30, verbose_name='论文英文名称')),
                ('paperChineseSummary', models.CharField(max_length=500, verbose_name='论文中文摘要')),
                ('paperEnglishSummary', models.CharField(max_length=500, verbose_name='论文英文摘要')),
                ('paperFiles', models.FileField(upload_to='', verbose_name='论文附件')),
                ('paperStatus', models.CharField(max_length=10, null=True, verbose_name='论文录用状态')),
            ],
            options={
                'verbose_name': '论文信息',
                'verbose_name_plural': '论文信息',
            },
        ),
        migrations.CreateModel(
            name='reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewerName', models.CharField(max_length=30, verbose_name='审稿专家姓名')),
                ('reviewerWorkplace', models.CharField(max_length=30, verbose_name='审稿专家工作单位')),
                ('reviewerTitle', models.CharField(max_length=30, verbose_name='审稿专家职称')),
                ('reviewerPhone', models.CharField(max_length=11, verbose_name='手机')),
                ('reviewerOfficePhone', models.CharField(max_length=30, verbose_name='办公电话')),
                ('reviewerEmail', models.CharField(max_length=30, verbose_name='邮件地址')),
                ('reviewerSecondEmail', models.CharField(max_length=30, verbose_name='备用邮箱')),
                ('reviewerBankName', models.CharField(max_length=30, verbose_name='银行名称')),
                ('reviewerBanknumber', models.CharField(max_length=30, verbose_name='银行账号')),
                ('reviewerMoney', models.CharField(max_length=30, verbose_name='审稿金额')),
                ('reviewernumber', models.CharField(max_length=30, verbose_name='审稿论文数')),
                ('journal', models.ManyToManyField(through='artical.inspect', to='artical.paper')),
            ],
            options={
                'verbose_name': '专家',
                'verbose_name_plural': '专家',
            },
        ),
        migrations.AddField(
            model_name='journal',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artical.paper'),
        ),
        migrations.AddField(
            model_name='inspect',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artical.paper'),
        ),
        migrations.AddField(
            model_name='inspect',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artical.reviewer'),
        ),
        migrations.AddField(
            model_name='author',
            name='paper',
            field=models.ManyToManyField(to='artical.paper'),
        ),
    ]
