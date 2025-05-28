from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
import requests




def home(request):
    return render(request, "home/index.html")


class hrMicroserviceView(APIView):
    def get(self, request):
        response = requests.get('http://localhost:8001/api/hrs/')
        return Response(response.json())


class payrolMicroserviceView(APIView):

    def get(self, request):
        response = requests.get('http://localhost:8002/api/payrols/')
        return Response(response.json())


class employeeMicroserviceView(APIView):
    def get(self, request):
        response = requests.get('http://localhost:8003/api/employees/')
        return Response(response.json())
