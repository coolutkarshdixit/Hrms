from rest_framework import generics
from .models import Payroluser
from .serializers import PayrolSerializer
from django.shortcuts import render
from .models import generate_monthly_areal_deduction, add_workday
from fpdf import FPDF


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

def generate_monthly_salary(request):
    return render (request, "home/generate_monthly_salary.html")

def update_monthly_salary(request):
    return render (request, "home/update_monthly_salary.html")

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

def report(request):
    
    sales = [
        {"item": "Keyboard", "amount": "$120,00"},
        {"item": "Mouse", "amount": "$10,00"},
        {"item": "House", "amount": "$1 000 000,00"},
    ]
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'Its a Monthly Payslip:',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)

    pdf.output('tuto1.pdf', 'F')
    return render(request, "index.html")
    
def registry(request):
    context = {}
    return render(request,"home/registry.html",context)
    
# def registry_data(request):
        
#     sales = [
#         {"item": "Employee_id", "amount": "$120,00" },
#         {"item": "Start_date", "amount": "$10,00"},
#         {"item": "Basic_pay", "amount": "$"},
#         {"item": "Hra", "amount": "$"},
#         {"item": "travel_allowance", "amount": "$"},
#         {"item": "food_allowance", "amount": "$"},
#         {"item": "special_allowance", "amount": "$"},
#         {"item": "car_allowance", "amount": "$"},
#         {"item": "petrol_allowance", "amount": "$"},
#         {"item": "driver_allowance", "amount": "$"},
#         {"item": "medical_allowance", "amount": "$"},
#         {"item": "internet_allowance", "amount": "$"},
#         {"item": "paper_allowance", "amount": "$"},
#         {"item": "epf", "amount": "$"},
#         {"item": "employer", "amount": "$"},
#         {"item": "employee_recovery", "amount": "$"},
#         {"item": "other_deduction", "amount": "$"},
#         {"item": "Gross_Salary", "amount": "$"},
        
#     ]
#     pdf = FPDF('L', 'mm', 'A4')
#     pdf.add_page()
#     pdf.set_font('courier', 'B', 16)
#     pdf.cell(40, 10, 'Its A Monthly Salary Details Registry:',0,1)
#     pdf.cell(40, 10, '',0,1)
#     pdf.set_font('courier', '', 12)
#     pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
#     pdf.line(10, 30, 150, 30)
#     pdf.line(10, 38, 150, 38)
#     for line in sales:
#         pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)

#     pdf.output('tuto2.pdf', 'F')
#     return render(request, "registry.html")



from fpdf import FPDF

def registry_data(request):
    sales = [
        {"item": "Employee_id", "amount": "$120,00"},
        {"item": "Start_date", "amount": "$10,00"},
        {"item": "Basic_pay", "amount": "$"},
        {"item": "Hra", "amount": "$"},
        {"item": "travel_allowance", "amount": "$"},
        {"item": "food_allowance", "amount": "$"},
        {"item": "special_allowance", "amount": "$"},
        {"item": "car_allowance", "amount": "$"},
        {"item": "petrol_allowance", "amount": "$"},
        {"item": "driver_allowance", "amount": "$"},
        {"item": "medical_allowance", "amount": "$"},
        {"item": "internet_allowance", "amount": "$"},
        {"item": "paper_allowance", "amount": "$"},
        {"item": "epf", "amount": "$"},
        {"item": "employer", "amount": "$"},
        {"item": "employee_recovery", "amount": "$"},
        {"item": "other_deduction", "amount": "$"},
        {"item": "Gross_Salary", "amount": "$"},
    ]
    
    # Create PDF in landscape format (L)
    pdf = FPDF('L', 'mm', 'A4')
    pdf.add_page()
    
    # Set the font
    pdf.set_font('courier', 'B', 16)
    
    # Title at the top
    pdf.cell(0, 10, 'Its A Monthly Salary Details Registry:', 0, 1, 'C')
    pdf.ln(10)  # Add space after title
    
    # Set font for the table headers
    pdf.set_font('courier', 'B', 12)
    
    # Define column widths for better spacing in landscape format
    column_width = 30  # width of each cell (adjust as needed)
    
    # Loop through the sales data and create table headers
    for line in sales:
        pdf.cell(column_width, 8, line['item'], 1, 0, 'C')  # Header: Item
    pdf.ln()  # Line break after header row
    
    # Set font for the table values
    pdf.set_font('courier', '', 12)
    
    # Loop through the sales data and display the corresponding amounts
    for line in sales:
        pdf.cell(column_width, 8, line['amount'], 1, 0, 'C')  # Values: Amount
    
    # Save the PDF file
    pdf.output('tuto2.pdf', 'F')
    
    return render(request, "registry.html")




