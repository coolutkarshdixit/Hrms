from django.contrib import admin
from django.contrib import messages
from shared_models.models import salary_add, new_employee, add_workday, generate_monthly_areal_deduction,  generate_monthly_salary


@admin.register(add_workday)
class AddWorkdayAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'month', 'payable_days']
    actions = ['generate_salary']

    def generate_salary(self, request, queryset):
        created_count = 0

        for work in queryset:
            try:
                salary = salary_add.objects.get(employee_id=work.employee_id)
            except salary_add.DoesNotExist:
                messages.warning(request, f"Salary not found for {work.employee_id}")
                continue

            if work.total_days == 0:
                messages.warning(request, f"Total days is zero for {work.employee_id} in {work.month}")
                continue

            ratio = work.payable_days / work.total_days

            # Avoid duplicates
            if generate_monthly_salary.objects.filter(employee_id=work.employee_id, month=work.month).exists():
                messages.info(request, f"Salary already exists for {work.employee_id} in {work.month}")
                continue

            generate_monthly_salary.objects.create(
                employee_id=salary.employee_id,
                month=work.month,
                basic_pay=round(salary.basic_pay * ratio, 2),
                hra=round(salary.hra * ratio, 2),
                travel_allowance=round(salary.travel_allowance * ratio, 2),
                food_allowance=round(salary.food_allowance * ratio, 2),
                special_allowance=round(salary.special_allowance * ratio, 2),
                car_allowance=round(salary.car_allowance * ratio, 2),
                petrol_allowance=round(salary.petrol_allowance * ratio, 2),
                driver_allowance=round(salary.driver_allowance * ratio, 2),
                medical_allowance=round(salary.medical_allowance * ratio, 2),
                internet_allowance=round(salary.internet_allowance * ratio, 2),
                paper_allowance=round(salary.paper_allowance * ratio, 2),
                epf=round(salary.epf * ratio, 2),
                employer=round(salary.employer * ratio, 2),
                employee_recovery=round(salary.employee_recovery * ratio, 2),
                other_deduction=round(salary.other_deduction * ratio, 2),
                total=round(salary.total * ratio, 2)
)

            created_count += 1

        messages.success(request, f"{created_count} salary records created.")
    generate_salary.short_description = "Generate Monthly Salary for selected employees"


# Register your models here.

admin.site.register(salary_add)
admin.site.register(new_employee)
admin.site.register(generate_monthly_salary)
admin.site.register(generate_monthly_areal_deduction)

