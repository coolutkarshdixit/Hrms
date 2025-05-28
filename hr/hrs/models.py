from django.db import models


class hr(models.Model):
    # User model fields
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

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
    
    def __str__(self):
        return self.first_name
    
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