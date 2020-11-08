# Generated by Django 3.1 on 2020-09-29 20:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeroomclass',
            name='school',
            field=models.ManyToManyField(to='schedules.School'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 29, 20, 5, 45, 971816, tzinfo=utc)),
        ),
    ]