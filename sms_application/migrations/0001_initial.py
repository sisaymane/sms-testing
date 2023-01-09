# Generated by Django 4.1.2 on 2023-01-09 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business_Unit_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_unit_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiative_type', models.CharField(blank=True, max_length=70, null=True, verbose_name=(('programme', 'programme'), ('project', 'project'), ('activity', 'activity'), ('task', 'task')))),
                ('initiative', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('KPI_ID', models.CharField(blank=True, max_length=400, null=True)),
                ('KPI', models.CharField(blank=True, max_length=300, null=True)),
                ('LOCAL_KPI_WEIGHT', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('GLOBAL_KPI_WEIGHT', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('KPI_WEIGHT_WITH_IN_PERSPECTIVE', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('weight_of_customer_perspective', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('weight_of_finance_perspective', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('weight_of_internal_process_perspective', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('weight_of_learning_and_growth_perspective', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization_Level_Strategic_Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategic_id', models.CharField(blank=True, max_length=70, null=True)),
                ('base_line', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('strategic_target', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('KPI_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms_application.kpi')),
            ],
        ),
        migrations.CreateModel(
            name='Perspective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perspective', models.CharField(max_length=80)),
                ('perspective_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('recommendation', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Strategic_Year',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('strategic_year', models.IntegerField(choices=[(2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040)], default=2023, verbose_name='year')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'strategic year',
                'verbose_name_plural': 'strategic year',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Target_By_Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KPI_ID', models.CharField(blank=True, max_length=40, null=True)),
                ('YEARLY_KPI_ID', models.CharField(blank=True, max_length=300, null=True)),
                ('THIS_YEAR_TARGET', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('strategic_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms_application.organization_level_strategic_target')),
                ('this_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='this_year', to='sms_application.strategic_year')),
            ],
        ),
        migrations.CreateModel(
            name='Tier_Level_One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_level_one_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision_statement', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Yearly_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polarity', models.CharField(blank=True, choices=[('High value indicate always good', 'High value indicate always good'), ('High value indicate always bad', 'High value indicate always bad'), ('High value may indicate good or bad', 'High value may indicate good or bad')], max_length=50, null=True)),
                ('last_year', models.CharField(blank=True, max_length=70, null=True)),
                ('last_year_performance', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('first_quarter_target', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('second_quarter_target', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('third_quarter_target', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('fourth_quarter_target', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('planned_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('HR_required', models.IntegerField(blank=True, null=True)),
                ('initiatives', models.CharField(blank=True, max_length=200, null=True)),
                ('YEARLY_KPI_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms_application.target_by_years')),
            ],
        ),
        migrations.CreateModel(
            name='Tier_Level_Two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_level_two_name', models.CharField(max_length=50)),
                ('tier_level_one_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_application.tier_level_one')),
            ],
        ),
        migrations.CreateModel(
            name='Tier_Level_Three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_level_three_name', models.CharField(max_length=50)),
                ('tier_level_two_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_application.tier_level_two')),
            ],
        ),
        migrations.CreateModel(
            name='Progress_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearly_report_id', models.CharField(max_length=30)),
                ('last_year_performance', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('first_quarter_progress', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('second_quarter_progress', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('second_quarter_score', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('third_quarter_progress', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('third_quarter_score', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('fourth_quarter_progress', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('fourth_quarter_score', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('good_to_and_from_bad_value_shift_point_on_target_direction', models.DecimalField(blank=True, decimal_places=2, help_text="this field required only if polarity value is 'High value may indicate good or bad'", max_digits=20, null=True)),
                ('planned_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('HR_required', models.IntegerField(blank=True, null=True, verbose_name='HR_required')),
                ('YEARLY_KPI_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms_application.yearly_plan')),
            ],
        ),
        migrations.AddField(
            model_name='organization_level_strategic_target',
            name='end_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='end', to='sms_application.strategic_year'),
        ),
        migrations.AddField(
            model_name='organization_level_strategic_target',
            name='start_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='start', to='sms_application.strategic_year'),
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective_id', models.CharField(blank=True, max_length=10, null=True)),
                ('objective', models.CharField(max_length=400)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('local_objective_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('global_objective_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_application.goal')),
                ('perspective', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sms_application.perspective')),
                ('responsible_body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sms_application.tier_level_one')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_statement', models.CharField(max_length=500)),
                ('vision_statement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_application.vision')),
            ],
        ),
        migrations.AddField(
            model_name='kpi',
            name='objective_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms_application.objective'),
        ),
        migrations.CreateModel(
            name='Initiative_KPI_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Key_Performance_Indicator', models.CharField(max_length=30)),
                ('initiative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sms_application.initiative')),
            ],
        ),
        migrations.AddField(
            model_name='initiative',
            name='objective',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sms_application.objective'),
        ),
        migrations.AddField(
            model_name='goal',
            name='mission_statement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_application.mission'),
        ),
        migrations.CreateModel(
            name='Business_Unit_Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_unit_objective', models.CharField(max_length=300)),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_application.objective')),
            ],
        ),
        migrations.CreateModel(
            name='Business_Unit_Action_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_unit_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_application.business_unit_list')),
                ('business_unit_objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_application.business_unit_objective')),
            ],
        ),
        migrations.CreateModel(
            name='Budgeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiative', models.CharField(max_length=300)),
                ('planned_budget', models.DecimalField(decimal_places=2, max_digits=20)),
                ('budget_title', models.CharField(max_length=40)),
                ('objective', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sms_application.objective')),
            ],
        ),
    ]
