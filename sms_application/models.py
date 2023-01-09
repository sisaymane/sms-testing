from django.db import models
import datetime
#from decimal import Decimal
#import decimal 
#for validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Avg, Count, Min, Sum, F, Count

# Create your models here.
class Vision(models.Model):
    vision_statement=models.CharField(max_length=400)
    def __str__(self):
        return str(self.vision_statement)
class Mission(models.Model):
    vision_statement=models.ForeignKey(Vision, on_delete=models.CASCADE)
    mission_statement=models.CharField(max_length=500)
    def __str__(self):
        return str(self.mission_statement)
class Goal(models.Model):
    mission_statement=models.ForeignKey(Mission, on_delete=models.CASCADE)
    goal=models.CharField(max_length=500)
    def __str__(self):
        return str(self.goal)
class Perspective(models.Model):
    perspective=models.CharField(max_length=80)
    perspective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    priority=models.IntegerField(null=True, blank=True)
    perspective_sum=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    recommendation=models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return str(self.perspective)
    def perspective_sum(self):
        total = Perspective.objects.aggregate(TOTAL = Sum('perspective_weight'))['TOTAL']
        return total
   
    #def recommendation(self):
   #     recommendation=None
  #      if self.perspective_sum() == 100 or self.perspective_sum()==1:
  #          recommendation='right'
 #       else:
 #           recommendation='make the sum of perspective weight is 100 or 1'
#        return recommendation
        
 
    def save(self, *args, **kwargs):
       
        super().save(*args, **kwargs)

class Tier_Level_One(models.Model):
    tier_level_one_name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.tier_level_one_name)
class Tier_Level_Two(models.Model):
    tier_level_one_name=models.ForeignKey(Tier_Level_One, on_delete=models.CASCADE)
    tier_level_two_name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.tier_level_two_name)
class Tier_Level_Three(models.Model):
    tier_level_two_name=models.ForeignKey(Tier_Level_Two, on_delete=models.CASCADE)
    tier_level_three_name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.tier_level_three_name)
class Objective(models.Model):
    #for test add and call mission you can leave from model and directly included in admin
    mission=models.CharField(max_length=300)
    goal=models.ForeignKey(Goal, on_delete=models.CASCADE)
    perspective=models.ForeignKey(Perspective, on_delete=models.SET_NULL, null=True, blank=True)
    perspective_weight=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    responsible_body=models.ForeignKey(Tier_Level_One, on_delete=models.SET_NULL, null=True, blank=True)
    objective_id=models.CharField(max_length=10, null=True, blank=True)
    objective=models.CharField(max_length=400)
    priority=models.IntegerField(null=True, blank=True)
    local_objective_weight=models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    global_objective_weight=models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_global_objective_weight=models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_weighted_customer_objective=models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_weighted_finance_objective=models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_weighted_internal_process_objective=models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_weighted_learning_and_growth_objective=models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    recommendation_for_weighting_alignment=models.CharField(max_length=200, null=True, blank=True)
    percentage_of_weighted_customer_objective=models.DecimalField(max_digits=10, decimal_places=3)
    percentage_of_weighted_finance_objective=models.DecimalField(max_digits=10, decimal_places=3)
    percentage_of_weighted_internal_process_objective=models.DecimalField(max_digits=10, decimal_places=3)
    percentage_of_weighted_learning_and_growth_objective=models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return str(self.objective)
    def mission(obj):
        return obj.goal.mission_statement
    def perspective_weight(obj):
        return obj.perspective.perspective_weight
        #checking for weight rating

    def percentage_of_weighted_customer_objective(self):
        ctr=Objective.objects.filter(perspective__perspective="customer").aggregate(TOTAL = Sum('local_objective_weight'))['TOTAL']
        return ctr
    def percentage_of_weighted_finance_objective(self):
        ctr=Objective.objects.filter(perspective__perspective="finance").aggregate(TOTAL = Sum('local_objective_weight'))['TOTAL']
        return ctr  
    def percentage_of_weighted_internal_process_objective(self):
        ctr=Objective.objects.filter(perspective__perspective="internal process").aggregate(TOTAL = Sum('local_objective_weight'))['TOTAL']
        return ctr    
    def percentage_of_weighted_learning_and_growth_objective(self):
        ctr=Objective.objects.filter(perspective__perspective="learning and growth").aggregate(TOTAL = Sum('local_objective_weight'))['TOTAL']
        return ctr    
    #checking for weight rating
    #recommend for weighting
    def recommendation_for_weighting_alignment(self):
        self.recommendation_for_weighting_alignment=None
        if self.percentage_of_weighted_finance_objective() is not None and self.percentage_of_weighted_finance_objective() > 100 and self.percentage_of_weighted_finance_objective() > 1 and self.percentage_of_weighted_finance_objective() < 100 and self.percentage_of_weighted_finance_objective() < 1: 
            self.recommendation_for_weighting_alignment = 'weighting finance objective is right'       

        else:
            self.recommendation_for_weighting_alignment = 'weigh finance objective is until the sum is 100 or 1'
        if self.percentage_of_weighted_customer_objective() is not None and self.percentage_of_weighted_customer_objective() > 100 and self.percentage_of_weighted_customer_objective() > 1 and self.percentage_of_weighted_customer_objective() < 100 and self.percentage_of_weighted_customer_objective() < 1: 
            self.recommendation_for_weighting_alignment = 'weighting customer objective is right'

        else:
            self.recommendation_for_weighting_alignment = 'weigh customer objective is until the sum is 100 or 1'

        if self.percentage_of_weighted_internal_process_objective() is not None and self.percentage_of_weighted_internal_process_objective() > 100 and self.percentage_of_weighted_internal_process_objective() > 1 and self.percentage_of_weighted_internal_process_objective() < 100 and self.percentage_of_weighted_internal_process_objective() < 1: 
            self.recommendation_for_weighting_alignment = 'weighting internal process objective is right'
   
        else:
            self.recommendation_for_weighting_alignment = 'weigh internal process objective is until the sum is 100 or 1'
        
        if self.percentage_of_weighted_learning_and_growth_objective() is not None and self.percentage_of_weighted_learning_and_growth_objective() > 100 and self.percentage_of_weighted_learning_and_growth_objective() > 1 and self.percentage_of_weighted_learning_and_growth_objective() < 100 and self.percentage_of_weighted_learning_and_growth_objective() < 1: 
            self.recommendation_for_weighting_alignment = 'weighting learning and growth objective is right'    
        else:
            self.recommendation_for_weighting_alignment = 'weigh learning and growth objective is until the sum is 100 or 1'
        return self.recommendation_for_weighting_alignment
       
        #----one one
    #calculate total objective weight
    def save(self, *args, **kwargs):
       # self.total_objective_weight==0.00
        if self.local_objective_weight <=100 and self.local_objective_weight >1:
            self.global_objective_weight=(self.local_objective_weight/100)*self.perspective_weight()
         #   return round(total_objective_weight, 2)
        if self.local_objective_weight <=1 and self.local_objective_weight >0:
            self.global_objective_weight=(self.local_objective_weight/1)*self.perspective_weight()
        #    return round(total_objective_weight, 2)
        super().save(*args, **kwargs)
    #calculate total objective weight
    #checking for weight perspective

    def total_global_objective_weight(self):
        sum= Objective.objects.aggregate(TOTAL = Sum('global_objective_weight'))['TOTAL']
        return sum
    def total_weighted_customer_objective(self):
        sum= Objective.objects.filter(perspective__perspective="customer").aggregate(TOTAL = Sum('global_objective_weight'))['TOTAL']
        return sum
    def total_weighted_finance_objective(self):
        sum= Objective.objects.filter(perspective__perspective="finance").aggregate(TOTAL = Sum('global_objective_weight'))['TOTAL']
        return sum
    def total_weighted_internal_process_objective(self):
        sum= Objective.objects.filter(perspective__perspective="internal process").aggregate(TOTAL = Sum('global_objective_weight'))['TOTAL']
        return sum
    def total_weighted_learning_and_growth_objective(self):
        sum= Objective.objects.filter(perspective__perspective="learning and growth").aggregate(TOTAL = Sum('global_objective_weight'))['TOTAL']
        return sum       
    #checking for weight perspective
    #-------
   # def total_objective_weight(self):
    #   tow=(self.objective_weight_from_particular_perspective/self.sum_of_objective_weight_from_particular_perspective())*self.perspective_weight()
   #    return round(tow, 2)
    
   # def save(self, *args, **kwargs):
  #      self.total_objective_weight=(self.objective_weight_from_particular_perspective/self.sum_of_objective_weight_from_particular_perspective())*self.perspective_weight()    
 #       super().save(*args, **kwargs)
 
    #--------

 
    #---customer perspective
  #  def recommendation_for_objective_weight(self):
     #   recommendation_for_objective_weight=None
    #    if self.new_perspective_weight()== self.total_objective_weight_sum():
   #         recommendation_for_objective_weight='aligned'
        
      #  if self.objective_weight_sum() == 100 or self.objective_weight_sum()==1:
     #       recommendation_for_objective_weight='right'
    #    else:
   #         recommendation_for_objective_weight='The sum of objective weight should be either 100 or 1'
 #       if self.perspective_weight() < self.total_objective_weight:
  #          recommendation_for_objective_weight='use the same indicator(particular scale) for perspective weight and objective weight, use either 100 or 1 as total for both perspective weight and objective weight'      
        # -*- coding=utf-8 -*-
      
#        return recommendation_for_objective_weight
    #--------customer
        

class Strategic_Year(models.Model):
    YEAR_CHOICES = [(r,r) for r in range(datetime.date.today().year-20, 2041)]
    id= models.AutoField(primary_key=True)        
    strategic_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return str(self.strategic_year)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'strategic year'
        verbose_name_plural = 'strategic year'
        #the whole plan
class KPI(models.Model):
    perspective=models.CharField(max_length=70, null=True, blank=True)
    perspective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    objective_id=models.ForeignKey(Objective, on_delete=models.CASCADE, null=True, blank=True)
    objective=models.CharField(max_length=300, null=True, blank=True)
    priority=models.IntegerField(null=True, blank=True)
    objective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    KPI_ID=models.CharField(max_length=400, null=True, blank=True)
    KPI=models.CharField(max_length=300, null=True, blank=True)
    LOCAL_KPI_WEIGHT=models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    GLOBAL_KPI_WEIGHT=models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    #gain from formula
    KPI_WEIGHT_WITH_IN_PERSPECTIVE=models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    weight_of_customer_perspective=models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    weight_of_finance_perspective=models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    weight_of_internal_process_perspective=models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    weight_of_learning_and_growth_perspective=models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.KPI_ID)
    #def objective_id(obj):
   #     return obj.objective_id.objective_id
    def objective(obj):
        return obj.objective_id.objective
    def objective_weight(obj):
        return obj.objective_id.global_objective_weight
    def perspective(obj):
        return obj.objective_id.perspective.perspective
    def perspective_weight(obj):
        return obj.objective_id.perspective.perspective_weight
    
class Organization_Level_Strategic_Target(models.Model):
    objective_id=models.CharField(max_length=30, null=True, blank=True)
    objective=models.CharField(max_length=300, null=True, blank=True)
    objective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    perspective=models.CharField(max_length=70, null=True, blank=True)
    perspective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    responsible_body=models.CharField(max_length=70, null=True, blank=True)
    strategic_id=models.CharField(max_length=70, null=True, blank=True)
    KPI_ID=models.ForeignKey(KPI, on_delete=models.CASCADE, null=True, blank=True)
    KPI=models.CharField(max_length=300, null=True, blank=True)
    base_line=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    strategic_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    start_year=models.ForeignKey(Strategic_Year, on_delete=models.SET_NULL, null=True, blank=True, related_name='start')
    end_year=models.ForeignKey(Strategic_Year, on_delete=models.SET_NULL, null=True, blank=True, related_name='end')
    def __str__(self):
        return str(self.strategic_id)
    def objective_id(obj):
         return obj.KPI_ID.objective_id.objective_id     
    def objective(obj):
        return obj.KPI_ID.objective_id.objective
    def objective_weight(obj):
        return obj.KPI_ID.objective_id.global_objective_weight
    def perspective(obj):
        return obj.KPI_ID.objective_id.perspective.perspective
    def perspective_weight(obj):
        return obj.KPI_ID.objective_id.perspective.perspective_weight
    def responsible_body(obj):
        return obj.KPI_ID.objective_id.responsible_body.tier_level_one_name
    def KPI(obj):
        return obj.KPI_ID.KPI
 #cascade to each year
class Target_By_Years(models.Model):
    objective_id=models.CharField(max_length=30, null=True, blank=True)
    objective=models.CharField(max_length=300, null=True, blank=True)
    objective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    perspective=models.CharField(max_length=70, null=True, blank=True)
    perspective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    responsible_body=models.CharField(max_length=60, null=True, blank=True)
    base_line=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    strategic_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    start_year=models.CharField(max_length=40, null=True, blank=True)
    end_year=models.CharField(max_length=40, null=True, blank=True)
    KPI_ID=models.CharField(max_length=40, null=True, blank=True)
    strategic_id=models.ForeignKey(Organization_Level_Strategic_Target, on_delete=models.CASCADE, null=True, blank=True)
    YEARLY_KPI_ID=models.CharField(max_length=300, null=True, blank=True)
    KPI=models.CharField(max_length=300, null=True, blank=True)
    this_year=models.ForeignKey(Strategic_Year, on_delete=models.SET_NULL, null=True, blank=True, related_name='this_year')
    THIS_YEAR_TARGET=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    base_line=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    strategic_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    start_year=models.ForeignKey(Strategic_Year, on_delete=models.SET_NULL, null=True, blank=True, related_name='start_year')
    end_year=models.ForeignKey(Strategic_Year, on_delete=models.SET_NULL, null=True, blank=True, related_name='end_year')
    def __str__(self):
        return str(self.YEARLY_KPI_ID) 
    def objective_id(obj):
        return obj.strategic_id.KPI_ID.objective_id.objective_id 
    def objective(obj):
        return obj.strategic_id.KPI_ID.objective_id.objective
    def objective_weight(obj):
        return obj.strategic_id.KPI_ID.objective_id.global_objective_weight
    def perspective(obj):
        return obj.strategic_id.KPI_ID.objective_id.perspective.perspective
    def perspective_weight(obj):
        return obj.strategic_id.KPI_ID.objective_id.perspective.perspective_weight
    def responsible_body(obj):
        return obj.strategic_id.KPI_ID.objective_id.responsible_body.tier_level_one_name
    def KPI_ID(obj):
        return obj.strategic_id.KPI_ID.KPI_ID
    def base_line(obj):
        return obj.strategic_id.base_line
    def strategic_target(obj):
        return obj.strategic_id.strategic_target
    def start_year(obj):
        return obj.strategic_id.start_year
    def end_year(obj):
        return obj.strategic_id.end_year   
    def KPI(obj):
        return obj.strategic_id.KPI_ID.KPI
   
    #cascade to months
class Yearly_Plan(models.Model):
    polarity_choices=(('High value indicate always good', 'High value indicate always good'), ('High value indicate always bad', 'High value indicate always bad'),
                      ('High value may indicate good or bad', 'High value may indicate good or bad'))
     #call from previous model instead of strategic year   
    perspective=models.CharField(max_length=70, null=True, blank=True)
    perspective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    responsible_body=models.CharField(max_length=70, null=True, blank=True)
    objective_id=models.CharField(max_length=40, null=True, blank=True)
    objective=models.CharField(max_length=300, null=True, blank=True)
    objective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    strategic_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  
    KPI_ID=models.CharField(max_length=70, null=True, blank=True)
    YEARLY_KPI_ID=models.ForeignKey(Target_By_Years, on_delete=models.CASCADE, null=True, blank=True)
    KPI=models.CharField(max_length=300, null=True, blank=True)
    this_year=models.CharField(max_length=50, null=True, blank=True)
    polarity=models.CharField(choices=polarity_choices, max_length=50, null=True, blank=True)
    base_line=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    #call from last year report both last year and last year performance
    last_year=models.CharField(max_length=70, null=True, blank=True)
    # -*- coding=utf-8 -*-
    last_year_kpi_id=models.ForeignKey('Progress_Report', on_delete=models.CASCADE, blank=True, null=True)

    last_year_performance=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    this_year_plan=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    this_year_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    first_quarter_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True) 
    second_quarter_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    third_quarter_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fourth_quarter_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    planned_budget=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    HR_required=models.IntegerField(null=True, blank=True)
    initiatives=models.CharField(max_length=200, null=True, blank=True)
    
    
#validation business process
#def remark(self):
  #      remark=None
        #if self.last_year_performance==None and (self.fourth_quarter_target!=None and self.third_quarter_target!=None and self.second_quarter_target!=None and self.first_quarter_target!=None and self.base_line()!=None) and (self.this_year_target()==self.fourth_quarter_target>=self.third_quarter_target>=self.second_quarter_target>=self.first_quarter_target>self.base_line()) and self.polarity=='High value indicate always good':
       #     remark='right'
      #      return remark
     #   elif self.last_year_performance!=None and (self.fourth_quarter_target!=None and self.third_quarter_target!=None and self.second_quarter_target!=None and self.first_quarter_target!=None) and (self.this_year_target()==self.fourth_quarter_target>=self.third_quarter_target>=self.second_quarter_target>=self.first_quarter_target>self.last_year_performance) and self.polarity=='High value indicate always good':
    #        remark='right' 
   #         return remark
  #      elif self.last_year_performance==None and (self.fourth_quarter_target!=None and self.third_quarter_target!=None and self.second_quarter_target!=None and self.first_quarter_target!=None and self.base_line()!=None) and (self.this_year_target()==self.fourth_quarter_target<=self.third_quarter_target<=self.second_quarter_target<=self.first_quarter_target<self.base_line()) and self.polarity=='High value indicate always bad':
 #           remark='right'
#            return remark
       # elif self.last_year_performance!=None and (self.fourth_quarter_target!=None and self.third_quarter_target!=None and self.second_quarter_target!=None and self.first_quarter_target!=None) and (self.this_year_target()==self.fourth_quarter_target<=self.third_quarter_target<=self.second_quarter_target<=self.first_quarter_target<self.last_year_performance) and self.polarity=='High value indicate always bad':
      #      remark='right' 
     #       return remark
    #    elif self.last_year_performance==None and (self.fourth_quarter_target!=None and self.third_quarter_target!=None and self.second_quarter_target!=None and self.first_quarter_target!=None and self.base_line()!=None and self.this_year_target()!=None) and (self.this_year_target()==self.fourth_quarter_target>=self.third_quarter_target>=self.second_quarter_target>=self.first_quarter_target>self.base_line() and self.base_line()<d) and self.polarity=='High value may indicate good or bad':
   #         remark='right' 
  #          return remark
 #       elif self.last_year_performance!=None and (self.fourth_quarter_target!=None and self.third_quarter_target!=None and self.second_quarter_target!=None and self.first_quarter_target!=None and self.this_year_target()!=None) and (self.this_year_target()==self.fourth_quarter_target>=self.third_quarter_target>=self.second_quarter_target>=self.first_quarter_target>self.last_year_performance and self.last_year_performance<d) and self.polarity=='High value may indicate good or bad':
        #    remark='right' 
       #     return remark
      #  elif self.last_year_performance==None and (self.fourth_quarter_target!=None and self.third_quarter_target!=None and self.second_quarter_target!=None and self.first_quarter_target!=None and self.base_line()!=None and self.this_year_target()!=None) and (d==self.fourth_quarter_target<=self.third_quarter_target<=self.second_quarter_target<=self.first_quarter_target<self.base_line() and self.base_line()>d) and self.polarity=='High value may indicate good or bad':
     #       remark='right' 
    #        return remark
   #     elif self.last_year_performance!=None and (self.fourth_quarter_target!=None and self.third_quarter_target!=None and self.second_quarter_target!=None and self.first_quarter_target!=None and self.this_year_target()!=None) and (self.this_year_target()==self.fourth_quarter_target<=self.third_quarter_target<=self.second_quarter_target<=self.first_quarter_target<self.last_year_performance and self.last_year_performance>d) and self.polarity=='High value may indicate good or bad':
  #          remark='right' 
 #           return remark
       # else:
      #      remark='wrong' 
     #   return remark
  
    def __str__(self):
        return str(self.YEARLY_KPI_ID)  
   
    def perspective(obj):
        return obj.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.perspective.perspective
    def perspective_weight(obj):
        return obj.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.perspective.perspective_weight   
    def objective_weight(obj):
        return obj.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.global_objective_weight
    def objective_id(obj):
        return obj.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.objective_id
    def objective(obj):
        return obj.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.objective
    def responsible_body(obj):
        return obj.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.responsible_body.tier_level_one_name  
    def this_year(obj):
        return obj.YEARLY_KPI_ID.this_year
    def KPI(obj):
        return obj.YEARLY_KPI_ID.strategic_id.KPI_ID.KPI
    def KPI_ID(obj):
        return obj.YEARLY_KPI_ID.strategic_id.KPI_ID
    def base_line(obj):
        return obj.YEARLY_KPI_ID.strategic_id.base_line
    def strategic_target(obj):
        return obj.YEARLY_KPI_ID.strategic_id.strategic_target
    def this_year_target(obj):
        return obj.YEARLY_KPI_ID.THIS_YEAR_TARGET
    def this_year_plan(self):
        this_year_plan=None
        if self.last_year_performance== None:
            this_year_plan=self.this_year_target()-self.base_line()
        else:
            this_year_plan=self.this_year_target()-self.last_year_performance 
        return this_year_plan
    #validation test
   

    def clean(self):
        a=self.first_quarter_target
        b=self.second_quarter_target
        c=self.third_quarter_target
        d=self.fourth_quarter_target
        
        e=self.YEARLY_KPI_ID.THIS_YEAR_TARGET
       # f=self.this_year_plan()
        
        x=self.base_line()
        y=self.last_year_performance
        
        p=self.polarity
   
     #general condition
        if e!=None and d!=None and e!=d:
            raise ValidationError('fourth quarter target should equal to this year target see this year target from strategic target')
     #fourth condition
        if y==None and x!=None and e!=None and c!=None and d!=None and p=='High value may indicate good or bad' and x>e and d>c:
            raise ValidationError({'fourth_quarter_target':'fourth quarter target should less than or equal to third quarter target with in this polarity perspective'}) 
        if y==None and x!=None and e!=None and c!=None and b!=None and p=='High value may indicate good or bad' and x>e and c>b:
            raise ValidationError({'third_quarter_target':'third quarter target should less than or equal to second quarter target with in this polarity perspective'}) 
        if y==None and x!=None and e!=None and a!=None and b!=None and p=='High value may indicate good or bad' and x>e and b>a:
            raise ValidationError({'second_quarter_target':'second quarter target should less than or equal to first quarter target with in this polarity perspective'}) 
     #fourth first
        if y==None and x!=None and e!=None and a!=None and p=='High value may indicate good or bad' and x>e and a>x:
            raise ValidationError({'first_quarter_target':'first quarter target should less than baseline with in this polarity perspective or make it blank if it is equal to baseline'})
     #fourth second
        if y!=None and e!=None and a!=None and p=='High value may indicate good or bad' and y>e and a>y:
            raise ValidationError({'third_quarter_target':'first quarter target should less than last year performance with in this polarity perspective'})
    #third condition
        if x!=None and e!=None and c!=None and d!=None and y==None and p=='High value may indicate good or bad' and x<e and c > d:
            raise ValidationError({'fourth_quarter_target':'fourth quarter target should greater than or equal to third quarter target with in this polarity perspective'}) 
        if x!=None and e!=None and b!=None and c!=None and y==None and p=='High value may indicate good or bad' and x<e and b > c:
            raise ValidationError({'third_quarter_target':'third quarter target should greater than or equal to second quarter target with in this polarity perspective'}) 
        if x!=None and e!=None and b!=None and y==None and p=='High value may indicate good or bad' and x<e and a > b:
            raise ValidationError({'second_quarter_target':'second quarter target should greater than or equal to first quarter target with in this polarity perspective'}) 
        #third first
        if x!=None and e!=None and a!=None and y==None and p=='High value may indicate good or bad' and x<e and x > a:
            raise ValidationError({'first_quarter_target':'first quarter target should greater than baseline with in this polarity perspective or make it blank if it is equal to baseline'}) 
        #third second
        if e!=None and y!=None and a!=None and p=='High value may indicate good or bad' and y<e and y > a:
            raise ValidationError({'first_quarter_target':'first quarter target should greater than last year performance with in this polarity perspective or make it blank if it is equal to last year performance'}) 
     
      #second condition
        if d!=None and c!=None and p!=None and p=='High value indicate always bad' and d>c:
            raise ValidationError({'fourth_quarter_target':'fourth quarter target should less than or equal to third quarter target with in this polarity perspective'})  
        if c!=None and b!=None and p!=None and p=='High value indicate always bad' and c>b:
            raise ValidationError({'third_quarter_target':'third quarter target should less than or equal to second quarter target with in this polarity perspective'})            
        if b!=None and a!=None and p!=None and p=='High value indicate always bad' and b>a:
            raise ValidationError({'second_quarter_target':'second quarter target should less than or equal to first quarter target with in this polarity perspective'})            
    #second first condition
        if y==None and a!=None and x!=None and p!=None and p=='High value indicate always bad' and a>x:
            raise ValidationError({'first_quarter_target':'first quarter target should less than baseline with in this polarity perspective or make it blank if it is equal to baseline'}) 
     #second second condition
        if y!=None and a!=None and p!=None and p=='High value indicate always bad' and a>y:
            raise ValidationError({'first_quarter_target':'first quarter target should less than last year performance with in this polarity perspective or make it blank if it is equal to last year performance'}) 
      #first condition and p=='High value indicate always good'

        if p!=None and d!=None and c!=None and p=='High value indicate always good' and d<c:
            raise ValidationError({'fourth_quarter_target':'fourth quarter target should greater or equal to third quarter target with in this polarity perspective'})
        if p!=None and c!=None and b!=None and p=='High value indicate always good' and c<b:
            raise ValidationError({'third_quarter_target':'third quarter target should greater or equal to second quarter target with in this polarity perspective'})
        if p!=None and b!=None and a!=None and p=='High value indicate always good' and b<a:
            raise ValidationError({'second_quarter_target':'second quarter target should greater or equal to first quarter target with in this polarity perspective'})
        #first first condition p=='High value indicate always good' y none
        if y==None and p!=None and a!=None and x!=None and p=='High value indicate always good' and a<x:
            raise ValidationError({'first_quarter_target':'first quarter target should greater than baseline with in this polarity perspective or make it blank if it is equal to baseline'})
        # first second condition p=='High value indicate always good' y not none
        if y!=None and p!=None and a!=None and p=='High value indicate always good' and a<y:
            raise ValidationError({'first_quarter_target':'first quarter target should greater than baseline with in this polarity perspective or make it blank if it is equal to baseline'})  
   
            
    #    if d!=None and e!=None and e>d or d<e and p=='High value indicate always good':target
                                  
   #         raise ValidationError(' fourth year quarter should equal to this year target ')
      
       # return remark
        
            
    #def annual(self):
    #    annual=None
   #     if  self.first_quarter is not None and self.second_quarter is not None and self.third_quarter is not None and self.fourth_quarter is not None:
  #          annual=self.first_quarter+self.second_quarter+self.third_quarter+self.fourth_quarter
 #       return annual

class Progress_Report(models.Model):
    yearly_report_id=models.CharField(max_length=30)
    perspective=models.CharField(max_length=70, null=True, blank=True)
    perspective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    responsible_body=models.CharField(max_length=70, null=True, blank=True)
    objective_id=models.CharField(max_length=40, null=True, blank=True)
    objective=models.CharField(max_length=300, null=True, blank=True)
    objective_weight=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    strategic_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  
    KPI_ID=models.CharField(max_length=70, null=True, blank=True)
    YEARLY_KPI_ID=models.ForeignKey(Yearly_Plan, on_delete=models.CASCADE, null=True, blank=True)
    KPI=models.CharField(max_length=300, null=True, blank=True)
    this_year=models.CharField(max_length=50, null=True, blank=True)
    polarity=models.CharField(max_length=50, null=True, blank=True)
    base_line=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    last_year_performance=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
   # last_year_kpi=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    #call from last year report both last year and last year performance
    this_year_plan=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    this_year_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    first_quarter_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True) 
    first_quarter_progress=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True) 
    first_quarter_score=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True) 
    second_quarter_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    second_quarter_progress=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    second_quarter_score=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True) 
    third_quarter_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    third_quarter_progress=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    third_quarter_score=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fourth_quarter_target=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fourth_quarter_progress=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fourth_quarter_score=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    good_to_and_from_bad_value_shift_point_on_target_direction=models.DecimalField(help_text="this field required only if polarity value is 'High value may indicate good or bad'", max_digits=20, decimal_places=2, null=True, blank=True)
   
    planned_budget=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    HR_required=models.IntegerField('HR_required', null=True, blank=True)
  #  remark=models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
   # initiatives=models.CharField(max_length=200, null=True, blank=True)  
    
    def __str__(self):
        return f"{self.yearly_report_id}, {self.fourth_quarter_progress}"# str(self.yearly_report_id)  
    def perspective(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.perspective.perspective
    def perspective_weight(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.perspective.perspective_weight   
    def objective_weight(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.global_objective_weight
    def objective_id(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.objective_id
    def objective(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.objective
    def responsible_body(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.KPI_ID.objective_id.responsible_body.tier_level_one_name 
    def this_year(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.this_year
    def KPI(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.KPI_ID.KPI
    def KPI_ID(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.KPI_ID
    def base_line(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.base_line
    def strategic_target(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.strategic_target
    def this_year_target(obj):
        return obj.YEARLY_KPI_ID.YEARLY_KPI_ID.THIS_YEAR_TARGET
    def this_year_plan(obj):
        return obj.YEARLY_KPI_ID.this_year_plan()
    def polarity(obj):
        return obj.YEARLY_KPI_ID.polarity
    def first_quarter_target(obj):
        return obj.YEARLY_KPI_ID.first_quarter_target
    def second_quarter_target(obj):
        return obj.YEARLY_KPI_ID.second_quarter_target
    def third_quarter_target(obj):
        return obj.YEARLY_KPI_ID.third_quarter_target
    def fourth_quarter_target(obj):
        return obj.YEARLY_KPI_ID.fourth_quarter_target
    #first
    def first_quarter_score(self):
        first_quarter_score=None
        #1
        if self.last_year_performance==None and (self.polarity()=='High value indicate always good' or self.polarity()=='High value indicate always bad'):
            first_quarter_score=(self.first_quarter_progress-self.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.base_line)/(self.YEARLY_KPI_ID.first_quarter_target-self.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.base_line)
            return round(first_quarter_score, 2)
        #2
        elif self.last_year_performance != None and (self.polarity()=='High value indicate always good' or self.polarity()=='High value indicate always bad'):
            first_quarter_score=(self.first_quarter_progress-self.last_year_performance)/(self.first_quarter_target()-self.last_year_performance)
            return round(first_quarter_score, 2)  
        #3  
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.base_line() is not None and (self.first_quarter_progress >= self.good_to_and_from_bad_value_shift_point_on_target_direction >= self.first_quarter_target() > self.base_line()) and self.last_year_performance==None and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=((self.good_to_and_from_bad_value_shift_point_on_target_direction-self.base_line())-(self.first_quarter_progress-self.good_to_and_from_bad_value_shift_point_on_target_direction))/(self.first_quarter_target()-self.base_line())
            return round(first_quarter_score, 2)          
       #4___________________________________________________________________________________________________________4
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.base_line() != None and (self.first_quarter_progress <= self.good_to_and_from_bad_value_shift_point_on_target_direction <= self.first_quarter_target() < self.base_line()) and self.last_year_performance==None and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=((self.good_to_and_from_bad_value_shift_point_on_target_direction-self.base_line())-(self.first_quarter_progress-self.good_to_and_from_bad_value_shift_point_on_target_direction))/(self.first_quarter_target()-self.base_line())
            return round(first_quarter_score, 2)           
       #5_
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.last_year_performance != None and (self.first_quarter_progress >= self.good_to_and_from_bad_value_shift_point_on_target_direction >= self.first_quarter_target() > self.last_year_performance) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=((self.good_to_and_from_bad_value_shift_point_on_target_direction-self.last_year_performance)-(self.first_quarter_progress-self.good_to_and_from_bad_value_shift_point_on_target_direction))/(self.first_quarter_target()-self.last_year_performance)
            return round(first_quarter_score, 2)   
        #6         
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.last_year_performance != None and (self.first_quarter_progress <= self.good_to_and_from_bad_value_shift_point_on_target_direction <= self.first_quarter_target() < self.last_year_performance) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=((self.good_to_and_from_bad_value_shift_point_on_target_direction-self.last_year_performance)-(self.first_quarter_progress-self.good_to_and_from_bad_value_shift_point_on_target_direction))/(self.first_quarter_target()-self.last_year_performance)
            return round(first_quarter_score, 2)             
       #7
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.base_line() != None and (self.good_to_and_from_bad_value_shift_point_on_target_direction >= self.first_quarter_progress > self.base_line()) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=(self.first_quarter_progress-self.base_line())/(self.first_quarter_target()-self.base_line())      
            return round(first_quarter_score, 2)   
        #8
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.base_line() != None and (self.good_to_and_from_bad_value_shift_point_on_target_direction <= self.first_quarter_progress <= self.base_line()) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=(self.first_quarter_progress-self.base_line())/(self.first_quarter_target()-self.base_line())           
            return round(first_quarter_score, 2)  
        #9   
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.last_year_performance != None and (self.good_to_and_from_bad_value_shift_point_on_target_direction >= self.first_quarter_progress > self.last_year_performance) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=(self.first_quarter_progress-self.last_year_performance)/(self.first_quarter_target()-self.last_year_performance)
            return round(first_quarter_score, 2)  
        #10 look for baseline is not none
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.last_year_performance != None and (self.good_to_and_from_bad_value_shift_point_on_target_direction <= self.first_quarter_progress < self.last_year_performance) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=(self.first_quarter_progress-self.last_year_performance)/(self.first_quarter_target()-self.last_year_performance)
            return round(first_quarter_score, 2) 
       #--11
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.base_line() != None and self.last_year_performance==None and (self.good_to_and_from_bad_value_shift_point_on_target_direction>=self.first_quarter_target()>self.base_line()>=self.first_quarter_progress) and  self.polarity()=='High value may indicate good or bad':
            first_quarter_score=(self.first_quarter_progress-self.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.base_line)/(self.YEARLY_KPI_ID.first_quarter_target-self.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.base_line)
            return round(first_quarter_score, 2)
        #12
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.base_line() != None and self.last_year_performance==None and (self.good_to_and_from_bad_value_shift_point_on_target_direction<=self.first_quarter_target()<self.base_line()<=self.first_quarter_progress) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=(self.first_quarter_progress-self.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.base_line)/(self.YEARLY_KPI_ID.first_quarter_target-self.YEARLY_KPI_ID.YEARLY_KPI_ID.strategic_id.base_line)
            return round(first_quarter_score, 2)
        #13
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.last_year_performance!=None and (self.good_to_and_from_bad_value_shift_point_on_target_direction>=self.first_quarter_target()>self.last_year_performance>=self.first_quarter_progress) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=(self.first_quarter_progress-self.last_year_performance)/(self.YEARLY_KPI_ID.first_quarter_target-self.last_year_performance)
            return round(first_quarter_score, 2)
        #14
        elif self.first_quarter_progress != None and self.good_to_and_from_bad_value_shift_point_on_target_direction != None and self.first_quarter_target() != None and self.last_year_performance!=None and (self.good_to_and_from_bad_value_shift_point_on_target_direction<=self.first_quarter_target()<self.last_year_performance<=self.first_quarter_progress) and self.polarity()=='High value may indicate good or bad':
            first_quarter_score=(self.first_quarter_progress-self.last_year_performance)/(self.YEARLY_KPI_ID.first_quarter_target-self.last_year_performance)
            return round(first_quarter_score, 2)
        else:
            return 'wrong data please fill the form again'  
    
    
    #second
   
  
     
  
   
class Initiative(models.Model):
    initiative_choices=(('programme', 'programme'), ('project', 'project'), ('activity', 'activity'), ('task', 'task'))
    objective=models.ForeignKey(Objective, on_delete=models.SET_NULL, null=True, blank=True)
  #  target=models.ForeignKey(Target, on_delete=models.SET_NULL, null=True, blank=True)
    initiative_type=models.CharField(initiative_choices, max_length=70, null=True, blank=True)
    initiative=models.CharField(max_length=200)
class Initiative_KPI_Type(models.Model):
    initiative=models.ForeignKey(Initiative, on_delete=models.CASCADE, null=True, blank=True)
    Key_Performance_Indicator=models.CharField(max_length=30)      
    def __str__(self):
        return str(self.Key_Performance_Indicator)
class Budgeting(models.Model):
    objective=models.ForeignKey(Objective, on_delete=models.SET_NULL, null=True, blank=True)
    initiative=models.CharField(max_length=300)
    planned_budget=models.DecimalField(max_digits=20 ,decimal_places=2)
    budget_title=models.CharField(max_length=40)
class Business_Unit_List(models.Model):
    business_unit_name=models.CharField(max_length=100)
    def __str__(self):
        return str(self.business_unit_name)
class Business_Unit_Objective(models.Model):
    objective=models.ForeignKey(Objective, on_delete=models.CASCADE)
    business_unit_objective=models.CharField(max_length=300)
    def __str__(self):
        return str(self.business_unit_objective)
class Business_Unit_Action_plan(models.Model):
    business_unit_name=models.ForeignKey(Business_Unit_List, on_delete=models.CASCADE)
    business_unit_objective=models.ForeignKey(Business_Unit_Objective, on_delete=models.CASCADE)