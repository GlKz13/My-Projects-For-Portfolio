# Generated by Django 4.1.1 on 2022-10-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_s', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='Номер телефона'),
        ),
    ]
