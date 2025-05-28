from django.db import models


class Payroluser(models.Model):
    # User model fields
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Master_monthly_workday(models.Model):
    month = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    generateStatus = models.CharField(max_length=100)
    updateStatus = models.CharField(max_length=100)
    finalisedStatus = models.CharField(max_length=100)
    
    def __str__(self):
        return self.month
    
class add_workday(models.Model):
    month = models.CharField(max_length=7,  unique=True)  # Stores in 'YYYY-MM' format
    total_days = models.IntegerField()
    employee_id = models.CharField(max_length=50, unique=True)
    employee_name = models.CharField(max_length=50, unique=True)
    leave =  models.IntegerField()
    weekends =  models.IntegerField()
    parity_off =  models.IntegerField()
    leave_without_pay =  models.IntegerField()
    workdays = models.FloatField()
    payable_days =  models.FloatField()
    
    
    def __str__(self):
        return self.month
    
    
    
class generate_monthly_areal_deduction(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    basic_pay = models.IntegerField()
    hra = models.IntegerField()
    travel_allowance = models.IntegerField()
    food_allowance = models.IntegerField()
    special_allowance = models.IntegerField()
    car_allowance = models.IntegerField()
    petrol_allowance = models.IntegerField()
    driver_allowance = models.IntegerField()
    medical_allowance = models.IntegerField()
    internet_allowance = models.IntegerField()
    paper_allowance = models.IntegerField()
    epf = models.IntegerField()
    employer = models.IntegerField()
    employee_recovery = models.IntegerField()
    other_deduction = models.IntegerField()
    taxes = models.IntegerField()
    remark = models.CharField(max_length=50, null=True, blank=True)
    total = models.FloatField()
    
    
    def __str__(self):
        return self.employee_id
    
class generate_monthly_salary(models.Model):
    employee_id = models.CharField(max_length=100)
    start_date = models.DateField()
    basic_pay = models.IntegerField()
    hra = models.IntegerField()
    travel_allowance = models.IntegerField()
    food_allowance = models.IntegerField()
    special_allowance = models.IntegerField()
    car_allowance = models.IntegerField()
    petrol_allowance = models.IntegerField()
    driver_allowance = models.IntegerField()
    medical_allowance = models.IntegerField()
    internet_allowance = models.IntegerField()
    paper_allowance = models.IntegerField()
    epf = models.IntegerField()
    employer = models.IntegerField()
    employee_recovery = models.IntegerField()
    Taxes = models.IntegerField()
    other_deduction = models.IntegerField()
    
    def __str__(self):
        return self.employee_id
    
