# Generated by Django 3.2 on 2021-04-25 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0008_auto_20210424_1925'),
        ('users', '0013_alter_studenthour_from_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenthour',
            name='cource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hour', to='cources.courses'),
        ),
    ]
