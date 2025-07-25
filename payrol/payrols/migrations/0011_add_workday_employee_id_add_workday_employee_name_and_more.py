# Generated by Django 5.1.4 on 2025-05-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrols', '0010_add_workday_workdays'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_workday',
            name='employee_id',
            field=models.CharField(default=21, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_workday',
            name='employee_name',
            field=models.CharField(default=22, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_workday',
            name='payable_days',
            field=models.FloatField(default=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='add_workday',
            name='month',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
