# Generated by Django 3.0.8 on 2020-10-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_investor_enter_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='invested_amt',
            field=models.FloatField(default=0),
        ),
    ]