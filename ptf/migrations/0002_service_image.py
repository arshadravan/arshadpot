# Generated by Django 3.1.2 on 2021-01-31 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='', upload_to='ptf/images'),
        ),
    ]
