# Generated by Django 4.1 on 2023-01-11 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_userinput_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileInput',
            new_name='FileInputModel',
        ),
    ]
