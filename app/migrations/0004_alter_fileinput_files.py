# Generated by Django 4.1 on 2023-01-11 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_fileinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinput',
            name='files',
            field=models.FileField(upload_to='excel/'),
        ),
    ]