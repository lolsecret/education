# Generated by Django 3.2 on 2021-04-25 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_teacherworktime_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherworktime',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
