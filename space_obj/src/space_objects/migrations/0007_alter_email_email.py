# Generated by Django 4.1 on 2022-09-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_objects', '0006_rename_eamil_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]