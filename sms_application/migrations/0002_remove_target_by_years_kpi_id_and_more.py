# Generated by Django 4.1.2 on 2023-01-09 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target_by_years',
            name='KPI_ID',
        ),
        migrations.RemoveField(
            model_name='yearly_plan',
            name='last_year_performance',
        ),
        migrations.AddField(
            model_name='yearly_plan',
            name='last_year_kpi_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms_application.progress_report'),
        ),
    ]
