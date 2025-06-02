from django.contrib import admin
from shared_models.models import salary_add
from shared_models.models import new_employee
from shared_models.models import add_workday
from shared_models.models import generate_monthly_areal_deduction

# Register your models here.

admin.site.register(salary_add)
admin.site.register(new_employee)
admin.site.register(add_workday)
admin.site.register(generate_monthly_areal_deduction)
