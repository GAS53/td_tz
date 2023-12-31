# Generated by Django 4.2.4 on 2023-08-13 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0003_driverlog_month_alter_driverlog_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverlog',
            name='year',
            field=models.SmallIntegerField(default=2000, validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(2000)], verbose_name='year now with status'),
        ),
    ]
