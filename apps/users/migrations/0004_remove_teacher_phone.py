# Generated by Django 3.2 on 2021-04-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_student_cources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='phone',
        ),
    ]