# Generated by Django 3.2 on 2021-04-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_studenthour_cource'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthour',
            name='cource_work_time',
            field=models.ManyToManyField(related_name='hour', to='users.TeacherWorkTime'),
        ),
    ]