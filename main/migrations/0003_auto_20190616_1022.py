# Generated by Django 2.2.2 on 2019-06-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_everything'),
    ]

    operations = [
        migrations.AlterField(
            model_name='everything',
            name='damage',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='everything',
            name='damage_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='everything',
            name='reaction_speed_rating',
            field=models.FloatField(default=0),
        ),
    ]
