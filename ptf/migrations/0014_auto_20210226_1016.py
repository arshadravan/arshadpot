# Generated by Django 3.1.2 on 2021-02-26 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptf', '0013_postcmnt_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcmnt',
            old_name='msg',
            new_name='mssg',
        ),
    ]
