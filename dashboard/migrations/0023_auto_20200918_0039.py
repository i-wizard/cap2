# Generated by Django 3.0.8 on 2020-09-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_receivers_date_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receivers',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]