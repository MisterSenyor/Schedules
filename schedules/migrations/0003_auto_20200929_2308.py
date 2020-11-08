# Generated by Django 3.1 on 2020-09-29 20:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20200929_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeroomclass',
            name='school',
        ),
        migrations.AddField(
            model_name='homeroomclass',
            name='schedule',
            field=models.ManyToManyField(to='schedules.Schedule'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 29, 20, 8, 44, 54096, tzinfo=utc)),
        ),
    ]
