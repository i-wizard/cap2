# Generated by Django 3.0.8 on 2020-09-13 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20200913_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservedreceivers',
            name='profile',
        ),
    ]