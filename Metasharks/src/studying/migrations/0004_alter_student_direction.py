# Generated by Django 4.1.2 on 2022-10-28 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studying', '0003_remove_student_age_student_curator_student_direction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studying.direction'),
        ),
    ]
