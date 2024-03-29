# Generated by Django 2.2.2 on 2019-06-16 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Everything',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('territory_name', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=256)),
                ('job_type_name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('status_name', models.CharField(max_length=100)),
                ('money', models.FloatField()),
                ('contract_ID', models.CharField(max_length=10)),
                ('executor_name', models.CharField(max_length=256)),
                ('real_start_date', models.DateTimeField()),
                ('real_end_date', models.DateTimeField()),
                ('comment', models.CharField(max_length=256)),
                ('comment_date', models.DateTimeField()),
                ('fix_date', models.DateTimeField()),
                ('fixed_too_late', models.BigIntegerField()),
                ('claims_during_fixes', models.BigIntegerField()),
                ('final_claims_after_fix', models.BigIntegerField()),
                ('damage_rating', models.FloatField()),
                ('reaction_speed_rating', models.FloatField()),
                ('damage', models.BigIntegerField()),
            ],
        ),
    ]
