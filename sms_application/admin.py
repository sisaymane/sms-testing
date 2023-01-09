from django.contrib import admin
from django.db.models import Avg, Count, Min, Sum

from .models import Vision, Mission, Goal, Objective, Tier_Level_One, Tier_Level_Two, Tier_Level_Three, KPI
from .models import  Strategic_Year, Perspective, Organization_Level_Strategic_Target, Target_By_Years, Yearly_Plan, Progress_Report
# Register your models here.
@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display=('vision_statement',)
    search_fields=('vision_statement',)
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display=('vision_statement', 'mission_statement')
    search_fields=('vision_statement__vision_statement', 'mission_statement')  
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display=('mission_statement', 'goal')
    search_fields=('mission_statement__mission_statement', 'goal')
@admin.register(Perspective)
class PerspectiveAdmin(admin.ModelAdmin):
    list_display=('perspective', 'priority', 'perspective_weight', 'perspective_sum', 'recommendation')
    search_fields=('perspective', 'perspective_weight')
@admin.register(Tier_Level_One)
class Tier_Level_OneAdmin(admin.ModelAdmin):
    list_display=('tier_level_one_name',)
    search_fields=('tier_level_one_name',)
@admin.register(Tier_Level_Two)
class Tier_Level_TwoAdmin(admin.ModelAdmin):
    list_display=('tier_level_two_name',)
    search_fields=('tier_level_one_name__tier_level_one_name', 'tier_level_two_name',)
@admin.register(Tier_Level_Three)
class Tier_Level_ThreeAdmin(admin.ModelAdmin):
    list_display=('tier_level_three_name',)
    search_fields=('tier_level_two_name__tier_level_two_name', 'tier_level_three_name',)
@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display=('mission', 'goal', 'perspective', 'perspective_weight', 'objective_id', 'objective', 'priority', 'local_objective_weight',                 
                   'global_objective_weight', 'responsible_body', 'total_global_objective_weight',
                   'total_weighted_customer_objective', 'total_weighted_finance_objective',
                   'total_weighted_internal_process_objective', 'total_weighted_learning_and_growth_objective',
                   'recommendation_for_weighting_alignment', 'percentage_of_weighted_customer_objective', 'percentage_of_weighted_finance_objective',
                   'percentage_of_weighted_internal_process_objective', 'percentage_of_weighted_learning_and_growth_objective',
                  )#
    exclude = ('global_objective_weight',) 
    search_fields=('goal__goal', 'perspective__perspective', 'objective_id', 'objective', 'total_objective_weight', 'responsible_body__tier_level_one_name',) 
   # readonly_fields = ['total_objective_weight', 'total_objective_weight_sum']
@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    list_display=('perspective', 'perspective_weight', 'objective_id', 'objective', 'objective_weight', 'KPI_ID', 'KPI', 'priority',
                  'LOCAL_KPI_WEIGHT', 'GLOBAL_KPI_WEIGHT', 'KPI_WEIGHT_WITH_IN_PERSPECTIVE', 'weight_of_customer_perspective',
                  'weight_of_finance_perspective', 'weight_of_internal_process_perspective', 'weight_of_learning_and_growth_perspective')
    search_fields=()
@admin.register(Organization_Level_Strategic_Target)
class Organization_Level_Strategic_TargetAdmin(admin.ModelAdmin):
    list_display=('objective_id','objective', 'objective_weight', 'perspective', 'perspective_weight', 'responsible_body',
                  'KPI_ID', 'KPI', 'base_line', 'strategic_target', 'start_year', 'end_year')
    search_fields=() 
@admin.register(Target_By_Years)
class Target_By_YearsAdmin(admin.ModelAdmin):
    list_display=('perspective', 'perspective_weight', 'objective_id', 'objective', 'objective_weight', 'responsible_body',
                  'base_line', 'strategic_target', 'start_year', 'end_year', 'KPI_ID', 'YEARLY_KPI_ID', 'KPI', 'this_year', 'THIS_YEAR_TARGET')
    search_fields=()      
     
@admin.register(Yearly_Plan)
class Yearly_PlanAdmin(admin.ModelAdmin):
   
    list_display=('perspective', 'perspective_weight', 'responsible_body', 'objective_id', 'objective', 'objective_weight', 'polarity',
                  'base_line', 'last_year', 'last_year_performance', 'this_year_target', 'this_year_plan', 'strategic_target', 'KPI_ID', 'YEARLY_KPI_ID', 'KPI', 'this_year', 
                   'first_quarter_target', 'second_quarter_target', 'third_quarter_target', 'fourth_quarter_target', 'planned_budget', 'HR_required', 'initiatives')
    search_fields=() 
   
@admin.register(Progress_Report) 
class Progress_ReportAdmin(admin.ModelAdmin):
    
    list_display=('yearly_report_id', 'perspective', 'perspective_weight', 'responsible_body', 'objective_id', 'objective',
                  'objective_weight', 'strategic_target', 'KPI_ID', 'KPI', 'this_year', 'polarity', 'YEARLY_KPI_ID',
                  'base_line', 'last_year_performance', 'this_year_plan', 'this_year_target', 'first_quarter_target', 'first_quarter_progress', 'first_quarter_score',
                  'second_quarter_target', 'second_quarter_progress', 'second_quarter_score', 
                  'third_quarter_target', 'third_quarter_progress', 'third_quarter_score', 'fourth_quarter_target', 'fourth_quarter_progress',
                  'fourth_quarter_score', 'good_to_and_from_bad_value_shift_point_on_target_direction', 'planned_budget')
        
    search_fields=() 
  

@admin.register(Strategic_Year)
class Strategic_YearAdmin(admin.ModelAdmin):
    list_display=('strategic_year',)
    search_fields=('strategic_year',)
    prepopulated_fields = {'slug': ('strategic_year',), }   
    #search_fields=('objective',)    
#@admin.register()
#class Admin(admin.ModelAdmin):
 # list_display=('')
  #search_fields=('',)
