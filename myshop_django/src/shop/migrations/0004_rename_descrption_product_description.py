# Generated by Django 4.1.1 on 2022-10-03 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_descrption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrption',
            new_name='description',
        ),
    ]
