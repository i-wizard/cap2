# Generated by Django 3.0.8 on 2020-09-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_ticket_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AddField(
            model_name='ticket',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
