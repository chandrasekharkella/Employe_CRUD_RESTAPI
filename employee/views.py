from django.shortcuts import render
from .models import Employee
from.serializer import Employeserialize
from rest_framework import viewsets



# Create your views here.
class Employe_crud(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class =Employeserialize