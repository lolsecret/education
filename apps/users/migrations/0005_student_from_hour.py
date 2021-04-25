# Generated by Django 3.2 on 2021-04-24 18:48

import apps.cources.service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_teacher_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='from_hour',
            field=models.TimeField(default='00:00', validators=[apps.cources.service.validate_round_hour]),
        ),
    ]