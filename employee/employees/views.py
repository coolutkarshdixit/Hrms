from rest_framework import generics
from .models import employee
from .serializers import employeeSerializer


class employeeListView(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer


class employeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer
