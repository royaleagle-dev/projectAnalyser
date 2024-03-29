# Generated by Django 2.2.13 on 2020-06-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(help_text='limit to 500 chars', max_length=500)),
                ('completed', models.BooleanField(default=False)),
                ('startDate', models.DateTimeField(auto_now=True)),
                ('endDate', models.DateTimeField(editable=False)),
                ('developer', models.CharField(max_length=100)),
            ],
        ),
    ]
