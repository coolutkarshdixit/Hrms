from django import forms

class GenerateSalaryForm(forms.Form):
    month = forms.CharField(label='Month (YYYY-MM)', max_length=7)
    employee_id = forms.CharField(label='Employee ID', max_length=50)
