# Generated by Django 2.2.2 on 2019-06-16 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_UID', models.BigIntegerField()),
                ('client_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executor_UID', models.BigIntegerField()),
                ('executor_name', models.CharField(max_length=256)),
                ('is_actual', models.BooleanField()),
                ('damage_rating', models.FloatField()),
                ('reaction_speed_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type_UID', models.BigIntegerField()),
                ('job_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SUID', models.BigIntegerField()),
                ('status_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TerritoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory_type_UID', models.BigIntegerField()),
                ('territory_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=256)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=256)),
                ('comment', models.CharField(max_length=256)),
                ('job_type_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.JobType')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_UID', models.BigIntegerField()),
                ('address', models.CharField(max_length=256)),
                ('year', models.IntegerField()),
                ('money', models.FloatField()),
                ('contract_ID', models.CharField(max_length=10)),
                ('real_start_date', models.DateTimeField()),
                ('real_end_date', models.DateTimeField()),
                ('fixed_too_late', models.BigIntegerField()),
                ('claims_during_fixes', models.BigIntegerField()),
                ('final_claims_after_fix', models.BigIntegerField()),
                ('client_UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
                ('executor_UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Executor')),
                ('job_type_UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.JobType')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Status')),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_UID', models.BigIntegerField()),
                ('comment', models.CharField(max_length=256)),
                ('comment_date', models.DateTimeField()),
                ('fix_date', models.DateTimeField()),
                ('damage', models.BigIntegerField()),
                ('contract_UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Contract')),
            ],
        ),
    ]
