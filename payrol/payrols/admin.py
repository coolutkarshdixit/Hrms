from django.contrib import admin
from payrols.models import generate_monthly_areal_deduction
from payrols.models import generate_monthly_salary
from payrols.models import add_workday


# Register your models here.


admin.site.register(generate_monthly_areal_deduction)
admin.site.register(generate_monthly_salary)
admin.site.register(add_workday)

