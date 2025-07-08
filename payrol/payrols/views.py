from rest_framework import generics
from .models import Payroluser
from .serializers import PayrolSerializer
from shared_models.models import generate_monthly_areal_deduction, add_workday
from fpdf import FPDF
from django.http import JsonResponse
from shared_models.models import add_workday, salary_add, generate_monthly_salary, new_employee
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Q
from collections import defaultdict
from decimal import Decimal
from django.db.models import Sum
from decimal import Decimal
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import get_template









class PayrolListView(generics.ListCreateAPIView):
    queryset = Payroluser.objects.all()
    serializer_class = PayrolSerializer


class PayrolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payroluser.objects.all()
    serializer_class =  PayrolSerializer

def home(request):
    return render(request, "home/index.html")

def generate_monthly_workday(request):
    return render (request, "home/generate_monthly_workday.html")

def add_monthly_workday(request):
    return render (request, "home/add_monthly_workday.html")

def update_monthly_workday(request):
    return render (request, "home/update_monthly_workday.html")

def finalised_monthly_workday(request):
    return render (request, "home/finalised_monthly_workday.html")

def generate_monthly_areal_deduction_view(request):
    return render (request, "home/generate_monthly_areal_deduction.html")


def add_workday_data(request):
    if request.method == "POST":
        month = request.POST.get("month")
        total_days = request.POST.get("total_days")
        employee_id = request.POST.get("employee_id")
        employee_name = request.POST.get("employee_name")
        leave = request.POST.get("leave")
        weekends = request.POST.get("weekends")
        parity_off = request.POST.get("parity_off")
        leave_without_pay = request.POST.get("leave_without_pay")
        workdays = float(request.POST.get('workdays', 0))
        payable_days = float(request.POST.get('payable_days', 0))

        try:
            add_workday.objects.update_or_create(month=month,
                                                total_days=total_days,
                                                employee_id=employee_id,
                                                employee_name=employee_name,
                                                leave=leave,
                                                weekends=weekends,
                                                parity_off=parity_off,
                                                leave_without_pay=leave_without_pay,
                                                workdays=workdays,
                                                payable_days=payable_days)
            return render(request,
                          "home/add_monthly_workday.html",
                          {"msg": "Order Price Details Submit"})
        except add_workday.DoesNotExist:
            return render(request,
                         "home/add_monthly_workday.html",
                          {"msg": "Order Price Details Already Added !!"})

def add_salary(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        start_date = request.POST.get("start_date")
        basic_pay = request.POST.get("basic_pay")
        hra = request.POST.get("hra")
        travel_allowance = request.POST.get("travel_allowance")
        food_allowance = request.POST.get("food_allowance")
        special_allowance = request.POST.get("special_allowance")
        car_allowance = request.POST.get("car_allowance")
        petrol_allowance = request.POST.get("petrol_allowance")
        driver_allowance = request.POST.get("driver_allowance")
        medical_allowance = request.POST.get("medical_allowance")
        internet_allowance = request.POST.get("internet_allowance")
        paper_allowance = request.POST.get("paper_allowance")
        epf = request.POST.get("epf")
        employer = request.POST.get("employer")
        employee_recovery = request.POST.get("employee_recovery")
        other_deduction = request.POST.get("other_deduction")
        taxes = request.POST.get("taxes")
        remark = request.POST.get("remark","")
        total = float(request.POST.get('total', 0))


        try:
            generate_monthly_areal_deduction.objects.update_or_create(employee_id=employee_id,
                                                start_date=start_date,
                                                basic_pay=basic_pay,
                                                hra=hra,
                                                travel_allowance=travel_allowance,
                                                food_allowance=food_allowance,
                                                special_allowance=special_allowance,
                                                car_allowance=car_allowance,
                                                petrol_allowance=petrol_allowance,
                                                driver_allowance=driver_allowance,
                                                medical_allowance=medical_allowance,
                                                internet_allowance=internet_allowance,
                                                paper_allowance=paper_allowance,
                                                epf=epf,
                                                employer=employer,
                                                employee_recovery=employee_recovery,
                                                other_deduction=other_deduction,
                                                taxes=taxes,
                                                remark=remark,
                                                total=total)
            return render(request,
                          "home/generate_monthly_areal_deduction.html",
                          {"msg": "Order Price Details Submit"})
        except generate_monthly_areal_deduction.DoesNotExist:
            return render(request,
                         "home/generate_monthly_areal_deduction.html",
                          {"msg": "Order Price Details Already Added !!"})

# def generate_monthly_salary(request):
#     return render (request, "home/generate_monthly_salary.html")


# def generate_monthly_salary_view(request):
#     months = [
#         ("01", "January"), ("02", "February"), ("03", "March"),
#         ("04", "April"), ("05", "May"), ("06", "June"),
#         ("07", "July"), ("08", "August"), ("09", "September"),
#         ("10", "October"), ("11", "November"), ("12", "December"),
#     ]
#     years = [str(y) for y in range(2020, 2999)]

#     if request.method == "POST":
#         month = request.POST.get("month")
#         year = request.POST.get("year")
#         employee_id_from = request.POST.get("employee_id_from", "").strip()
#         employee_id_to = request.POST.get("employee_id_to", "").strip()
#         location = request.POST.get("location", "").strip()

#         filters = {}

#         # Use lexicographical string comparison (for alphanumeric IDs)
#         if employee_id_from and employee_id_to:
#             if employee_id_from > employee_id_to:
#                 messages.error(request, "From Employee ID cannot be greater than To Employee ID.")
#                 return redirect("generate_monthly_salary_view")

#             filters["employee_id__gte"] = employee_id_from
#             filters["employee_id__lte"] = employee_id_to
#         elif employee_id_from:
#             filters["employee_id__gte"] = employee_id_from
#         elif employee_id_to:
#             filters["employee_id__lte"] = employee_id_to

#         if location:
#             filters["location__icontains"] = location

#         salary_records = salary_add.objects.filter(**filters)
#         if not salary_records.exists():
#             messages.error(request, "No employees found with provided filters.")
#             return redirect("generate_monthly_salary_view")

#         month_str = f"{year}-{int(month):02d}"
#         generated = []

#         for salary in salary_records:
#             emp_id = salary.employee_id
#             try:
#                 work = add_workday.objects.get(employee_id=emp_id, month=month_str)
#                 if work.total_days == 0:
#                     continue
#                 ratio = work.payable_days / work.total_days

#                 _, created = generate_monthly_salary.objects.update_or_create(
#                     employee_id=emp_id,
#                     month=month_str,
#                     defaults={
#                         "basic_pay": salary.basic_pay * ratio,
#                         "hra": salary.hra * ratio,
#                         "travel_allowance": salary.travel_allowance * ratio,
#                         "food_allowance": salary.food_allowance * ratio,
#                         "special_allowance": salary.special_allowance * ratio,
#                         "car_allowance": salary.car_allowance * ratio,
#                         "petrol_allowance": salary.petrol_allowance * ratio,
#                         "driver_allowance": salary.driver_allowance * ratio,
#                         "medical_allowance": salary.medical_allowance * ratio,
#                         "internet_allowance": salary.internet_allowance * ratio,
#                         "paper_allowance": salary.paper_allowance * ratio,
#                         "epf": salary.epf * ratio,
#                         "employer": salary.employer * ratio,
#                         "employee_recovery": salary.employee_recovery * ratio,
#                         "other_deduction": salary.other_deduction * ratio,
#                         "total": salary.total * ratio
#                     }
#                 )
#                 generated.append(emp_id)
#             except add_workday.DoesNotExist:
#                 messages.warning(request, f"Workday not found for Employee ID {emp_id}")
#             except Exception as e:
#                 messages.warning(request, f"Error for Employee ID {emp_id}: {str(e)}")

#         if generated:
#             messages.success(request, f"Salary generated for {len(generated)} employee(s).")
#         else:
#             messages.error(request, "No salary generated.")

#         return redirect("generate_monthly_salary_view")

#     return render(request, "home/generate_monthly_salary.html", {
#         "months": months,
#         "years": years
#     })




def generate_monthly_salary_view(request):
    months = [
        ("01", "January"), ("02", "February"), ("03", "March"),
        ("04", "April"), ("05", "May"), ("06", "June"),
        ("07", "July"), ("08", "August"), ("09", "September"),
        ("10", "October"), ("11", "November"), ("12", "December"),
    ]
    years = [str(y) for y in range(2020, 2999)]

    if request.method == "POST":
        month = request.POST.get("month")
        year = request.POST.get("year")
        employee_id_from = request.POST.get("employee_id_from", "").strip()
        employee_id_to = request.POST.get("employee_id_to", "").strip()
        location = request.POST.get("location", "").strip()
        department = request.POST.get("department", "").strip()

        employee_filters = {}

        if employee_id_from and employee_id_to:
            if employee_id_from > employee_id_to:
                messages.error(request, "From Employee ID cannot be greater than To Employee ID.")
                return redirect("generate_monthly_salary_view")
            employee_filters["employee_id__gte"] = employee_id_from
            employee_filters["employee_id__lte"] = employee_id_to
        elif employee_id_from:
            employee_filters["employee_id__gte"] = employee_id_from
        elif employee_id_to:
            employee_filters["employee_id__lte"] = employee_id_to

        if location and location != "All Locations":
            employee_filters["location__icontains"] = location

        if department:
            employee_filters["department__icontains"] = department

        # Step 1: Get filtered employee_ids from new_employee
        employee_ids = new_employee.objects.filter(**employee_filters).values_list("employee_id", flat=True)

        # Step 2: Use these IDs to get corresponding salary records
        salary_records = salary_add.objects.filter(employee_id__in=employee_ids)

        if not salary_records.exists():
            messages.error(request, "No employees found with provided filters.")
            return redirect("generate_monthly_salary_view")

        month_str = f"{year}-{int(month):02d}"
        generated = []

        for salary in salary_records:
            emp_id = salary.employee_id
            try:
                work = add_workday.objects.get(employee_id=emp_id, month=month_str)
                if work.total_days == 0:
                    continue
                ratio = work.payable_days / work.total_days

                _, created = generate_monthly_salary.objects.update_or_create(
                    employee_id=emp_id,
                    month=month_str,
                    defaults={
                        "basic_pay": salary.basic_pay * ratio,
                        "hra": salary.hra * ratio,
                        "travel_allowance": salary.travel_allowance * ratio,
                        "food_allowance": salary.food_allowance * ratio,
                        "special_allowance": salary.special_allowance * ratio,
                        "car_allowance": salary.car_allowance * ratio,
                        "petrol_allowance": salary.petrol_allowance * ratio,
                        "driver_allowance": salary.driver_allowance * ratio,
                        "medical_allowance": salary.medical_allowance * ratio,
                        "internet_allowance": salary.internet_allowance * ratio,
                        "paper_allowance": salary.paper_allowance * ratio,
                        "epf": salary.epf * ratio,
                        "employer": salary.employer * ratio,
                        "employee_recovery": salary.employee_recovery * ratio,
                        "other_deduction": salary.other_deduction * ratio,
                        "total": salary.total * ratio
                    }
                )
                generated.append(emp_id)
            except add_workday.DoesNotExist:
                messages.warning(request, f"Workday not found for Employee ID {emp_id}")
            except Exception as e:
                messages.warning(request, f"Error for Employee ID {emp_id}: {str(e)}")

        if generated:
            messages.success(request, f"Salary generated for {len(generated)} employee(s).")
        else:
            messages.error(request, "No salary generated.")

        return redirect("generate_monthly_salary_view")

    return render(request, "home/generate_monthly_salary.html", {
        "months": months,
        "years": years,
        "locations": new_employee.objects.values_list("location", flat=True).distinct(),
        "departments": new_employee.objects.values_list("department", flat=True).distinct()
    })



def update_monthly_salary(request):
    return render (request, "home/update_monthly_salary.html")

def finalised_monthly_salary(request):
    return render (request, "home/finalised_monthly_salary.html")

# Its a Monthly Salary Generation And calculation function start from here on :-
def generate_finalised_monthly_salary(request):
    return render (request, "home/finalised_monthly_salary.html")

            
def index(request):
    context = {}
    return render(request,"index.html",context)




# def generate_monthly_registry_view(request):
#     # Fetch salary and areal deduction records
#     salary_qs = generate_monthly_salary.objects.all()
#     areal_qs = generate_monthly_areal_deduction.objects.all()

#     # Optionally fetch employee info (for location)
#     employee_info = {
#         emp.employee_id: emp for emp in new_employee.objects.all()
#     }

#     # Combine and group by location and then employee_id
#     grouped_data = defaultdict(lambda: defaultdict(dict))

#     # Salary data
#     for sal in salary_qs:
#         emp_id = sal.employee_id
#         location = employee_info.get(emp_id).location if emp_id in employee_info else "Unknown"
#         grouped_data[location][emp_id]['salary'] = sal

#     # Areal data
#     for ded in areal_qs:
#         emp_id = ded.employee_id
#         location = employee_info.get(emp_id).location if emp_id in employee_info else "Unknown"
#         grouped_data[location][emp_id]['areal'] = ded

#     # Structure it for the template
#     structured_data = []
#     for location, employees in grouped_data.items():
#         emp_list = []
#         for emp_id, records in employees.items():
#             emp_list.append({
#                 "employee_id": emp_id,
#                 "location": location,
#                 "salary": records.get("salary"),
#                 "areal": records.get("areal")
#             })
#         structured_data.append({
#             "location": location,
#             "employees": emp_list
#         })

#     return render(request, "home/generate_monthly_registry.html", {
#         "grouped_data": structured_data
#     })


# from decimal import Decimal
# from django.shortcuts import render
# from shared_models.models import generate_monthly_salary, generate_monthly_areal_deduction, new_employee
# from collections import defaultdict

# def safe_decimal(value):
#     try:
#         return Decimal(value or 0)
#     except:
#         return Decimal(0)

# def generate_monthly_registry_view(request):
#     salary_qs = generate_monthly_salary.objects.all()
#     areal_qs = generate_monthly_areal_deduction.objects.all()
#     employee_info = {e.employee_id: e for e in new_employee.objects.all()}

#     grouped = defaultdict(list)

#     # Grand totals across all locations
#     all_location_totals = defaultdict(Decimal)

#     for emp_id in set(list(salary_qs.values_list("employee_id", flat=True)) + list(areal_qs.values_list("employee_id", flat=True))):
#         salary = salary_qs.filter(employee_id=emp_id).first()
#         areal = areal_qs.filter(employee_id=emp_id).first()
#         emp = employee_info.get(emp_id)
#         location = emp.location if emp else "Unknown"

#         # Per-employee totals (salary + areal)
#         emp_total = {}
#         keys = [
#             "basic_pay", "hra", "travel_allowance", "food_allowance",
#             "special_allowance", "car_allowance", "petrol_allowance",
#             "driver_allowance", "medical_allowance", "internet_allowance",
#             "paper_allowance", "epf", "employer", "employee_recovery",
#             "other_deduction", "total"
#         ]

#         for key in keys:
#             val1 = safe_decimal(getattr(salary, key, 0))
#             val2 = safe_decimal(getattr(areal, key, 0))
#             emp_total[key] = val1 + val2
#             all_location_totals[key] += emp_total[key]

#         grouped[location].append({
#             "employee_id": emp_id,
#             "salary": salary,
#             "areal": areal,
#             "total_row": emp_total
#         })

#     return render(request, "home/generate_monthly_registry.html", {
#         "grouped_data": grouped.items(),
#         "grand_total": all_location_totals,
#     })
from decimal import Decimal
from shared_models.models import generate_monthly_salary, generate_monthly_areal_deduction, new_employee
from collections import defaultdict

def safe_decimal(value):
    try:
        return Decimal(value or 0)
    except:
        return Decimal(0)

def generate_monthly_registry_view(request):
    salary_qs = generate_monthly_salary.objects.all()
    areal_qs = generate_monthly_areal_deduction.objects.all()
    employee_info = {e.employee_id: e for e in new_employee.objects.all()}

    grouped = defaultdict(list)
    all_location_totals = defaultdict(Decimal)

    keys = [
        "basic_pay", "hra", "travel_allowance", "food_allowance",
        "special_allowance", "car_allowance", "petrol_allowance",
        "driver_allowance", "medical_allowance", "internet_allowance",
        "paper_allowance", "epf", "employer", "employee_recovery",
        "other_deduction", "taxes", "total"
    ]

    all_employee_ids = set(salary_qs.values_list("employee_id", flat=True)) | set(areal_qs.values_list("employee_id", flat=True))

    location_wise_group = defaultdict(lambda: {
        "employees": [],
        "location_total": defaultdict(Decimal)
    })

    for emp_id in all_employee_ids:
        salary = salary_qs.filter(employee_id=emp_id).first()
        areal = areal_qs.filter(employee_id=emp_id).first()
        emp = employee_info.get(emp_id)
        location = emp.location if emp else "Unknown"

        emp_total = {}

        for key in keys:
            val1 = safe_decimal(getattr(salary, key, 0))
            val2 = safe_decimal(getattr(areal, key, 0))
            total_val = val1 + val2
            emp_total[key] = total_val

            all_location_totals[key] += total_val
            location_wise_group[location]["location_total"][key] += total_val

        location_wise_group[location]["employees"].append({
            "employee_id": emp_id,
            "salary": salary,
            "areal": areal,
            "total_row": emp_total
        })

    # Flatten data for template
    grouped_data = [
        (location, data["employees"], data["location_total"])
        for location, data in location_wise_group.items()
    ]

    return render(request, "home/generate_monthly_registry.html", {
        "grouped_data": grouped_data,
        "grand_total": all_location_totals,
    })




def generate_payslip_view(request):
    employee_ids = new_employee.objects.values_list("employee_id", flat=True).distinct()
    locations = new_employee.objects.values_list("location", flat=True).distinct()
    departments = new_employee.objects.values_list("department", flat=True).distinct()

    months = [f"{i:02}" for i in range(1, 13)]
    years = [str(y) for y in range(2024, datetime.now().year + 12)]

    return render(request, "home/generate_payslip_form.html", {
        "employee_ids": employee_ids,
        "locations": locations,
        "departments": departments,
        "months": months,
        "years": years,
    })


from django.shortcuts import render
from decimal import Decimal
from shared_models.models import (
    generate_monthly_salary,
    generate_monthly_areal_deduction,
    new_employee,
    add_workday
)
from datetime import datetime

def filtered_payslip_view(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    employee_id_from = request.GET.get('employee_id_from')
    employee_id_to = request.GET.get('employee_id_to')
    department = request.GET.get('department')
    location = request.GET.get('location')

    selected_month = month
    selected_year = year

    filters = {}
    if employee_id_from:
        filters['employee_id__gte'] = employee_id_from
    if employee_id_to:
        filters['employee_id__lte'] = employee_id_to
    if department:
        filters['department'] = department
    if location:
        filters['location'] = location

    employees = new_employee.objects.filter(**filters)
    results = []

    for emp in employees:
        employee_id = emp.employee_id
        month_str = f"{year}-{month.zfill(2)}"  # format 'YYYY-MM'

        # Fetch salary and areal deduction records
        salary = generate_monthly_salary.objects.filter(employee_id=employee_id, month=month_str).first()
        areal = generate_monthly_areal_deduction.objects.filter(employee_id=employee_id).first()

        # Convert to dictionaries
        salary_dict = vars(salary) if salary else {}
        areal_dict = vars(areal) if areal else {}

        # Clean non-field keys
        salary_dict = {k: v for k, v in salary_dict.items() if not k.startswith("_")}
        areal_dict = {k: v for k, v in areal_dict.items() if not k.startswith("_")}

        # Merge salary + areal into total
        total = {}
        for key in set(salary_dict.keys()).union(areal_dict.keys()):
            val1 = salary_dict.get(key, Decimal(0))
            val2 = areal_dict.get(key, Decimal(0))

            if isinstance(val1, (int, float)):
                val1 = Decimal(val1)
            if isinstance(val2, float):
                val2 = Decimal(str(val2))

            try:
                total[key] = val1 + val2
            except:
                total[key] = val1 or val2  # for strings (e.g., remarks)

        # Get payable days from add_workday
        workday = add_workday.objects.filter(employee_id=employee_id, month=month_str).first()
        payable_days = workday.payable_days if workday else None

        results.append({
            'employee': emp,
            'salary': salary_dict,
            'areal': areal_dict,
            'total': total,
            'payable_days': payable_days
        })

    # Define the display order and labels of components
    component_keys = [
        ('basic_pay', 'Basic Pay'),
        ('hra', 'HRA'),
        ('travel_allowance', 'Travel Allowance'),
        ('food_allowance', 'Food Allowance'),
        ('special_allowance', 'Special Allowance'),
        ('car_allowance', 'Car Allowance'),
        ('petrol_allowance', 'Petrol Allowance'),
        ('driver_allowance', 'Driver Allowance'),
        ('medical_allowance', 'Medical Allowance'),
        ('internet_allowance', 'Internet Allowance'),
        ('paper_allowance', 'Paper Allowance'),
        ('epf', 'EPF'),
        ('employer', 'Employer'),
        ('employee_recovery', 'Employee Recovery'),
        ('other_deduction', 'Other Deduction'),
        ('taxes', 'Taxes'),
        ('remark', 'Remark'),
        ('total', 'Total'),
    ]

    return render(request, 'home/filtered_payslip_results.html', {
        'results': results,
        'selected_month': selected_month,
        'selected_year': selected_year,
        'component_keys': component_keys,
    })


# views.py

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from reportlab.pdfgen import canvas
from decimal import Decimal
from shared_models.models import new_employee, generate_monthly_salary, generate_monthly_areal_deduction

@csrf_exempt
def download_payslip_pdf(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        month = request.POST.get("month")
        year = request.POST.get("year")
        month_str = f"{year}-{int(month):02d}"

        employee = new_employee.objects.filter(employee_id=employee_id).first()
        if not employee:
            return HttpResponse("Employee not found.", status=404)

        salary = generate_monthly_salary.objects.filter(employee_id=employee_id, month=month_str).first()
        areal = generate_monthly_areal_deduction.objects.filter(employee_id=employee_id).first()

        if not salary:
            return HttpResponse("Salary data not found.", status=404)

        def safe_decimal(val):
            try:
                return Decimal(val or 0)
            except:
                return Decimal(0)

        fields = [
            "basic_pay", "hra", "travel_allowance", "food_allowance",
            "special_allowance", "car_allowance", "petrol_allowance",
            "driver_allowance", "medical_allowance", "internet_allowance",
            "paper_allowance", "epf", "employer", "employee_recovery",
            "other_deduction", "taxes", "total"
        ]

        salary_data = {field: safe_decimal(getattr(salary, field, 0)) for field in fields}
        areal_data = {field: safe_decimal(getattr(areal, field, 0)) for field in fields} if areal else {field: Decimal(0) for field in fields}
        total_data = {field: salary_data[field] + areal_data[field] for field in fields}

        html = render_to_string("home/payslip_template.html", {
            "employee": employee,
            "salary": salary_data,
            "areal": areal_data,
            "total": total_data,
            "month": month_str,
            "year": year
        })

        from weasyprint import HTML
        pdf_file = BytesIO()
        HTML(string=html).write_pdf(target=pdf_file)
        pdf_file.seek(0)

        filename = f"payslip_{employee_id}_{month_str}.pdf"
        response = HttpResponse(pdf_file.read(), content_type="application/pdf")
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response

    return HttpResponse("Invalid request", status=400)
