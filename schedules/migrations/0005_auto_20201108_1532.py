# Generated by Django 3.1 on 2020-11-08 13:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_auto_20200929_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 8, 13, 32, 55, 381898, tzinfo=utc)),
        ),
    ]
