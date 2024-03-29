# Generated by Django 2.2.2 on 2019-06-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190616_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executor_name', models.CharField(max_length=100)),
                ('foundation_date', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='everything',
            name='accident_weight',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='everything',
            name='shift_weight',
            field=models.BigIntegerField(),
        ),
    ]
