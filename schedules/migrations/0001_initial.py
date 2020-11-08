# Generated by Django 3.1 on 2020-09-25 13:36

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=800)),
                ('_id', models.IntegerField(default=0)),
                ('homeRoom', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.TextField(default='none')),
                ('name', models.CharField(default='none', max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(default='none')),
                ('date', models.DateField(default=datetime.datetime(2020, 9, 25, 13, 36, 55, 393272, tzinfo=utc))),
                ('schedule_class', models.ManyToManyField(to='schedules.ScheduleClass')),
                ('school', models.ManyToManyField(to='schedules.School')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(default='none', max_length=800)),
                ('day1', models.ManyToManyField(related_name='day1', to='schedules.ScheduleClass')),
                ('day2', models.ManyToManyField(related_name='day2', to='schedules.ScheduleClass')),
                ('day3', models.ManyToManyField(related_name='day3', to='schedules.ScheduleClass')),
                ('day4', models.ManyToManyField(related_name='day4', to='schedules.ScheduleClass')),
                ('day5', models.ManyToManyField(related_name='day5', to='schedules.ScheduleClass')),
                ('day6', models.ManyToManyField(related_name='day6', to='schedules.ScheduleClass')),
                ('school', models.ManyToManyField(null=True, to='schedules.School')),
            ],
        ),
        migrations.CreateModel(
            name='HomeroomClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('classes', models.ManyToManyField(to='schedules.ScheduleClass')),
            ],
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('personal_changes', models.TextField(default='none')),
                ('classes', models.ManyToManyField(to='schedules.ScheduleClass')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('schedule', models.ManyToManyField(to='schedules.Schedule')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]