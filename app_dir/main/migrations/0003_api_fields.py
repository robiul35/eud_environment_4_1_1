# Generated by Django 2.2.3 on 2019-08-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190801_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='fields',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
