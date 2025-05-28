"""
URL configuration for gateways project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('generate_monthly_workday', views.generate_monthly_workday),
    path('update_monthly_workday', views.update_monthly_workday),
    path('add_monthly_workday', views.add_monthly_workday),
    path('finalised_monthly_workday', views.finalised_monthly_workday),
    path('generate_monthly_areal_deduction_view', views.generate_monthly_areal_deduction_view),
    path('generate_monthly_salary', views.generate_monthly_salary),
    path('update_monthly_salary', views.update_monthly_salary),
    path('finalised_monthly_salary', views.finalised_monthly_salary),
    path('index', views.index),
    path('report', views.report),
    path('registry', views.registry),
    path('add_workday_data', views.add_workday_data),
    path('add_salary', views.add_salary),
    path('registry_data', views.registry_data),
    # path('export_report', views.export_report),


]
 