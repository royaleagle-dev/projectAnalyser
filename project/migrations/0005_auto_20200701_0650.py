# Generated by Django 2.2.13 on 2020-07-01 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200701_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='startDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
