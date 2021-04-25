# Generated by Django 3.2 on 2021-04-25 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210425_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='test_datetime',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='wotk_datetime',
        ),
        migrations.RemoveField(
            model_name='teacherworktime',
            name='weekday',
        ),
        migrations.AddField(
            model_name='teacherworktime',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 25, 8, 45, 22, 685632), unique=True),
        ),
    ]
