# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruminate', '0002_auto_20171202_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Office_Hours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_live', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruminate.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('time_created', models.DateTimeField(auto_now=True)),
                ('is_answered', models.BooleanField(default=False)),
                ('office_hour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruminate.Office_Hours')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('course_enrolled', models.ManyToManyField(related_name='_user_course_enrolled_+', to='ruminate.Course')),
                ('course_teaching', models.ManyToManyField(related_name='_user_course_teaching_+', to='ruminate.Course')),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.AddField(
            model_name='office_hours',
            name='teaching_assistant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruminate.User'),
        ),
    ]