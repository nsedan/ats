# Generated by Django 3.1.6 on 2021-03-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0009_auto_20210323_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
