# Generated by Django 2.2.8 on 2020-08-11 20:26

import datetime
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
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, null=True)),
                ('value', models.CharField(max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=60, null=True)),
            ],
            options={
                'verbose_name_plural': 'Actuators',
            },
        ),
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('api', models.CharField(max_length=100, null=True)),
                ('fields', models.TextField(max_length=500, null=True)),
                ('connection', models.TextField(max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'API',
            },
        ),
        migrations.CreateModel(
            name='Interactive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('fields', models.TextField(max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Interactive',
            },
        ),
        migrations.CreateModel(
            name='MailBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('api', models.FileField(blank=True, null=True, upload_to='mailbox')),
            ],
            options={
                'verbose_name_plural': 'MailBox',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, null=True)),
                ('value', models.CharField(max_length=100, null=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('name', models.CharField(max_length=60, null=True)),
            ],
            options={
                'verbose_name_plural': 'Sensors',
            },
        ),
        migrations.CreateModel(
            name='ServiceRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('service_type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Service Registry',
            },
        ),
        migrations.CreateModel(
            name='SaveComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100, null=True)),
                ('code', models.TextField(max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SaveComposition',
            },
        ),
    ]
