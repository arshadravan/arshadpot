# Generated by Django 3.1.2 on 2021-02-21 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptf', '0008_auto_20210221_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutm',
            name='brief',
            field=models.CharField(max_length=5000),
        ),
    ]
