"""
URL configuration for payrol project.

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
from django.contrib import admin
from django.urls import path, include
from payrols.views import PayrolListView, PayrolDetailView

urlpatterns = [
    path('',include('payrols.urls')),
    path('admin/', admin.site.urls),
    path('api/payrols/', PayrolListView.as_view(), name='Payrol-list'),
    path('api/payrols/<int:pk>/', PayrolDetailView.as_view(), name='Payrol-detail'),
]
