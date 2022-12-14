# Generated by Django 4.1.2 on 2022-10-30 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studying', '0006_student_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='curator',
        ),
        migrations.AddField(
            model_name='curator',
            name='curator_direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studying.direction'),
        ),
        migrations.AddField(
            model_name='direction',
            name='curator_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='studying.curator'),
        ),
    ]
