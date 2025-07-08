from django.db import models

# Create your models here.

    
class salary_add(models.Model):
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
    total = models.FloatField()
    
    def __str__(self):
        return self.employee_id
    


class new_employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    wife_name = models.CharField(max_length=100)
    current_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    no_of_kids = models.IntegerField()
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    marriage_anniversary_date = models.DateField()
    status = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    bank_account_no = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)
    epf_no = models.CharField(max_length=50)
    
    
    def __str__(self):
        
        return self.first_name

   
class add_workday(models.Model):
    month = models.CharField(max_length=7,  )  # Stores in 'YYYY-MM' format
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
    


class generate_monthly_salary(models.Model):
    employee_id = models.CharField(max_length=50)
    month = models.CharField(max_length=7)  # Format 'YYYY-MM'
    
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2)
    travel_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    food_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    car_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    petrol_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    driver_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    internet_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    paper_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    epf = models.DecimalField(max_digits=10, decimal_places=2)
    employer = models.DecimalField(max_digits=10, decimal_places=2)
    employee_recovery = models.DecimalField(max_digits=10, decimal_places=2)
    other_deduction = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee_id} - {self.month}"


    

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
    