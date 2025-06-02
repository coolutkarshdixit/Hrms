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
                                                status=status)
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

def employee_list(request):
    # email = request.session['email']
    r = new_employee.objects.all()
    return render(request, "home/employee_list.html",
                  {'data': r})

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
def salary_details_list(request):
    r = salary_add.objects.all()
    return render(request,"home/salary_details_list.html",
                  {'data': r})
            
# def salary_details_list(request):
#     return render(request,"home/salary_details_list.html")

def salary_increment_details(request):
    r = salary_add.objects.all()
    return render(request,"home/salary_increment_details.html",
                  {'data': r})

# def salary_increment_details(request):
#     return render(request,"home/salary_increment_details.html")

class hrListView(generics.ListCreateAPIView):
    queryset = hr.objects.all()
    serializer_class = hrSerializer


class hrDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = hr.objects.all()
    serializer_class = hrSerializer
