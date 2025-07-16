from rest_framework import generics
from .models import hr
from .serializers import hrSerializer
from django.shortcuts import render
from shared_models.models import new_employee,salary_add


def home(request):
    return render(request, "home/index.html")

# def employee_list(request):
#     return render(request, "home/employee_list.html")


def employee_add_details(request):
    return render(request, "home/employee_add_details.html")

def add_details(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        department = request.POST.get("department")
        location = request.POST.get("location")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        wife_name = request.POST.get("wife_name")
        current_address = request.POST.get("current_address")
        permanent_address = request.POST.get("permanent_address")
        no_of_kids = request.POST.get("no_of_kids")
        date_of_birth = request.POST.get("date_of_birth")
        date_of_joining = request.POST.get("date_of_joining")
        marriage_anniversary_date = request.POST.get("marriage_anniversary_date")
        status = request.POST.get("status")
        bank_name = request.POST.get("bank_name")
        bank_account_no = request.POST.get("bank_account_no")
        ifsc_code = request.POST.get("ifsc_code")
        epf_no = request.POST.get("epf_no")
        # t = itemno+itemname+itemprice+services+gst+sgst
        try:
            new_employee.objects.update_or_create(employee_id=employee_id,
                                                first_name=first_name,
                                                last_name=last_name,
                                                department=department,
                                                location=location,
                                                father_name=father_name,
                                                mother_name=mother_name,
                                                wife_name=wife_name,
                                                current_address=current_address,
                                                permanent_address=permanent_address,
                                                no_of_kids=no_of_kids,
                                                date_of_birth=date_of_birth,
                                                date_of_joining=date_of_joining,
                                                marriage_anniversary_date=marriage_anniversary_date,
                                                status=status,bank_name=bank_name,bank_account_no=bank_account_no,ifsc_code=ifsc_code,epf_no=epf_no)
            return render(request,
                          "home/employee_add_details.html",
                          {"msg": "Order Price Details Submit"})
        except new_employee.DoesNotExist:
            return render(request,
                         "home/employee_add_details.html",
                          {"msg": "Order Price Details Already Added !!"})

# def add_details(request):
#     if request.method == "POST":
#         data = {
#             "employee_id": request.POST.get("employee_id"),
#             "firstname": request.POST.get("firstname"),
#             "lastname": request.POST.get("lastname"),
#             "father_name": request.POST.get("father_name"),
#             "mother_name": request.POST.get("mother_name"),
#             "wife_name": request.POST.get("wife_name"),
#             "current_address": request.POST.get("current_address"),
#             "permanent_address": request.POST.get("permanent_address"),
#             "no_of_kids": request.POST.get("no_of_kids"),
#             "date_of_birth": request.POST.get("date_of_birth"),
#             "date_of_joining": request.POST.get("date_of_joining"),
#             "marriage_anniversary_date": request.POST.get("marriage_anniversary_date"),
#             "status": request.POST.get("status"),
#         }
#         try:
#             new_employee.objects.create(**data)
#             return render(request,"home/employee_add_details.html",
#                           {"msg": "Details Submit"})
#         except new_employee.DoesNotExist: 
#             return render(request,"home/employee_add_details.html",
#                           {"msg": "Details Already Submit"})

from django.shortcuts import render
from shared_models.models import new_employee

def employee_list(request):
    employees = new_employee.objects.exclude(employee_id__isnull=True).exclude(employee_id__exact="")

    # Ensure clean, URL-safe employee_ids
    for emp in employees:
        if emp.employee_id:
            emp.employee_id = emp.employee_id.strip().replace(" ", "").replace("\u200b", "")

    return render(request, "home/employee_list.html", {'data': employees})



def edit_employee(request, employee_id):
    employee = get_object_or_404(new_employee, employee_id=employee_id)
    if request.method == "POST":
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.department = request.POST.get('department')
        employee.location = request.POST.get('location')
        employee.father_name = request.POST.get('father_name')
        employee.mother_name = request.POST.get('mother_name')
        employee.wife_name = request.POST.get('wife_name')
        employee.current_address = request.POST.get('current_address')
        employee.permanent_address = request.POST.get('permanent_address')
        employee.no_of_kids = request.POST.get('no_of_kids')
        employee.date_of_birth = request.POST.get('date_of_birth')
        employee.date_of_joining = request.POST.get('date_of_joining')
        employee.marriage_anniversary_date = request.POST.get('marriage_anniversary_date')
        employee.status = request.POST.get('status')
        employee.bank_name = request.POST.get('bank_name')
        employee.bank_account_no = request.POST.get('bank_account_no')
        employee.ifsc_code = request.POST.get('ifsc_code')
        employee.epf_no = request.POST.get('epf_no')
        employee.save()
        return redirect('employee_list')  # this will now work after fixing urls.py
    return render(request, "home/edit_employee.html", {'employee': employee})

def employee_details(request):
    # email = request.session['email']
    r = new_employee.objects.all()
    return render(request, "home/employee_list.html",
                  {'data': r})


    
# def employee_details(request):
#     template_name = "employeedetails.html"
#     data = {'data': new_employee.objects.all()}
#     return render(request, template_name, data)

def employee_view_list(request):
    return render(request, "home/employee_view_list.html")
def employee_update_list(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        wife_name = request.POST.get("wife_name")
        current_address = request.POST.get("current_address")
        permanent_address = request.POST.get("permanent_address")
        no_of_kids = request.POST.get("no_of_kids")
        date_of_birth = request.POST.get("date_of_birth")
        date_of_joining = request.POST.get("date_of_joining")
        marriage_anniversary_date = request.POST.get("marriage_anniversary_date")
        status = request.POST.get("status")

        try:
            user_profile_data = new_employee.objects.get(employee_id=employee_id)
        except new_employee.DoesNotExist:
            print("Not Found")
        else:
            user_profile_data.employee_id = employee_id
            user_profile_data.firstname = firstname
            user_profile_data.lastname = lastname
            user_profile_data.father_name = father_name
            user_profile_data.mother_name = mother_name
            user_profile_data.wife_name = wife_name
            user_profile_data.current_address = current_address
            user_profile_data.permanent_address = permanent_address
            user_profile_data.no_of_kids = no_of_kids
            user_profile_data.date_of_birth = date_of_birth
            user_profile_data.date_of_joining = date_of_joining
            user_profile_data.marriage_anniversary_date = marriage_anniversary_date
            user_profile_data.status = status
            user_profile_data.save(update_fields=[
                'employee_id',
                'firstname',
                'lastname',
                'father_name',
                'mother_name',
                'wife_name',
                'current_address',
                'permanent_address',
                'no_of_kids',
                'date_of_birth',
                'date_of_joining',
                'marriage_anniversary_date',
                'status',])
            return render(request, "home/employee_update_list.html",
                          {'data': user_profile_data})

    # return render(request, "home/employee_update_list.html",)
    
def create_salary_details(request):
    return render(request, "home/create_salary_details.html")    

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
        total = float(request.POST.get('total', 0))

        try:
            salary_add.objects.update_or_create(employee_id=employee_id,
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
                                                total=total)
            return render(request,
                          "home/create_salary_details.html",
                          {"msg": "Order Price Details Submit"})
        except salary_add.DoesNotExist:
            return render(request,
                         "home/create_salary_details.html",
                          {"msg": "Order Price Details Already Added !!"})
            
from django.shortcuts import render, get_object_or_404, redirect
from shared_models.models import salary_add, new_employee

# Show salary list
def salary_details_list(request):
    salary_records = salary_add.objects.all()
    data = []

    for record in salary_records:
        emp = new_employee.objects.filter(employee_id=record.employee_id).first()
        data.append({
            'employee_id': record.employee_id,
            'first_name': emp.first_name if emp else '',
            'last_name': emp.last_name if emp else '',
            'department': emp.department if emp else '',
            'date_of_joining': emp.date_of_joining if emp else '',
            'status': emp.status if emp else '',
        })

    return render(request, "home/salary_details_list.html", {'data': data})


# Edit salary details for employee
def edit_salary_add(request, employee_id):
    salary = get_object_or_404(salary_add, employee_id=employee_id)

    if request.method == "POST":
        salary.basic_pay = request.POST.get('basic_pay')
        salary.hra = request.POST.get('hra')
        salary.travel_allowance = request.POST.get('travel_allowance')
        salary.food_allowance = request.POST.get('food_allowance')
        salary.special_allowance = request.POST.get('special_allowance')
        salary.save()
        return redirect('salary_details_list')

    return render(request, "home/edit_salary_add.html", {'salary': salary})




            
# def salary_details_list(request):
#     return render(request,"home/salary_details_list.html")

def salary_increment_details(request):
    salary_records = salary_add.objects.all()
    data = []

    for record in salary_records:
        emp = new_employee.objects.filter(employee_id=record.employee_id).first()
        data.append({
            'employee_id': record.employee_id,
            'first_name': emp.first_name if emp else '',
            'last_name': emp.last_name if emp else '',
            'department': emp.department if emp else '',
            'date_of_joining': emp.date_of_joining if emp else '',
            'status': emp.status if emp else '',
        })

    return render(request, "home/salary_increment_details.html", {'data': data})


# def salary_increment_details(request):
#     return render(request,"home/salary_increment_details.html")

class hrListView(generics.ListCreateAPIView):
    queryset = hr.objects.all()
    serializer_class = hrSerializer


class hrDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = hr.objects.all()
    serializer_class = hrSerializer
