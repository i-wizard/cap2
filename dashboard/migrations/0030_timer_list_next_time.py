# Generated by Django 3.0.8 on 2020-09-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_timer_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='list_next_time',
            field=models.DateTimeField(null=True),
        ),
    ]
