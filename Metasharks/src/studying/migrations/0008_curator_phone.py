# Generated by Django 4.1.2 on 2022-10-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studying', '0007_remove_direction_curator_curator_curator_direction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curator',
            name='phone',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
