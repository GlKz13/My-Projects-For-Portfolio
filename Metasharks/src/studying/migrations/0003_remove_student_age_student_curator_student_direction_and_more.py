# Generated by Django 4.1.2 on 2022-10-28 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studying', '0002_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='curator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='studying.curator'),
        ),
        migrations.AddField(
            model_name='student',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studying.curator'),
        ),
        migrations.AddField(
            model_name='student',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studying.discipline'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studying.direction'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studying.group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
