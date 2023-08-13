# Generated by Django 4.2.4 on 2023-08-13 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='company_id')),
                ('full_name', models.CharField(max_length=200, verbose_name='full company name')),
                ('short_name', models.CharField(max_length=50, verbose_name='full company name')),
            ],
        ),
        migrations.CreateModel(
            name='DriverStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='not activ', max_length=10, verbose_name='value')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='driverapp.company')),
                ('driver_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='driverapp.driverstatus')),
            ],
        ),
    ]
