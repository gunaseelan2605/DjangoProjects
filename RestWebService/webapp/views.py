from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import Employee
from webapp.serializers import EmployeeSerializer

class EmployeeController(APIView):
    def get(self,request):
        employee = Employee.objects.all()
        print(employee)
        serializer = EmployeeSerializer(employee,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
