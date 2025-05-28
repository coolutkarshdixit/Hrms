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
    path('employee_add_details/',views.employee_add_details),
    path('employee_add_details/add_details',views.add_details),
    path('employee_list/',views.employee_list),
    path('employee_details',views.employee_details, name='employee_details'),
    path('employee_view_list/',views.employee_view_list),
    path('employee_update_list/',views.employee_update_list),
    path('create_salary_details/',views.create_salary_details),
    path('create_salary_details/add_salary',views.add_salary),
    path('salary_details_list/',views.salary_details_list),
    path('salary_increment_details/',views.salary_increment_details),

]
 