# Generated by Django 4.2.4 on 2023-08-13 20:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0002_driverlog_day_driverlog_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverlog',
            name='month',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)], verbose_name='month now with status'),
        ),
        migrations.AlterField(
            model_name='driverlog',
            name='day',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(0)], verbose_name='day now with status'),
        ),
        migrations.AlterField(
            model_name='driverlog',
            name='time',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)], verbose_name='count ours with status'),
        ),
    ]
