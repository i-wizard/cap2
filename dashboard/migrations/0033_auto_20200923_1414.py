# Generated by Django 3.0.8 on 2020-09-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_receivers_is_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receivers',
            name='is_mod',
            field=models.IntegerField(default=0),
        ),
    ]
