# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-21 20:32
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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=3)),
                ('course_number', models.CharField(max_length=3)),
                ('section', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('days', models.CharField(max_length=25)),
                ('time', models.CharField(max_length=25)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('absences', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.Course')),
            ],
        ),
    ]
