# Generated by Django 3.2 on 2021-04-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0004_auto_20210424_1806'),
        ('users', '0002_auto_20210424_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cources',
            field=models.ManyToManyField(to='cources.Courses'),
        ),
    ]
