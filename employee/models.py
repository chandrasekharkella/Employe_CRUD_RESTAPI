from django.db import models


# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(unique=True)
    empname=models.CharField(max_length=100)
    empemail=models.CharField(max_length=50)
    phone=models.IntegerField()
    password=models.CharField(max_length=15)
    empaddress=models.CharField(max_length=200)

    def __str__(self):
        return self.empname

