# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-19 09:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('roles', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True, null=True)),
                ('story', models.TextField(blank=True, null=True)),
                ('planned_date_start', models.DateField(blank=True, null=True)),
                ('planned_date_end', models.DateField(blank=True, null=True)),
                ('participant_optional_cities', models.CharField(blank=True, max_length=255, null=True)),
                ('photographer_optional_city', models.CharField(blank=True, max_length=255, null=True)),
                ('photographer_schedule', models.IntegerField(blank=True, null=True)),
                ('volunteer_schedule', models.IntegerField(blank=True, null=True)),
                ('skill', models.IntegerField(blank=True, choices=[(1, '文案、文字编辑、活动策划'), (2, '平面/VI/网页/UI设计'), (3, '被拍者社群运营管理'), (4, '网站开发')], null=True)),
                ('will', models.IntegerField(blank=True, choices=[(1, '文案、文字编辑、活动策划'), (2, '平面/VI/网页/UI设计'), (3, '被拍者社群运营管理'), (4, '网站开发')], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('google_calendar_event_created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaigns.Campaign'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
