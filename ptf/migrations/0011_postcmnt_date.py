# Generated by Django 3.1.2 on 2021-02-23 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptf', '0010_postcmnt'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcmnt',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 23, 19, 30, 15, 523444)),
        ),
    ]
