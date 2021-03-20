# Generated by Django 3.1.6 on 2021-03-19 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_auto_20210318_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='muscles_worked',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='workout',
            name='workout_program',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='workout',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workouts.category'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workouts.workouttype'),
        ),
    ]
