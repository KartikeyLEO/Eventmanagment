from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.CharField(primary_key=True,max_length=10)
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)

class Guest(models.Model):
    guestid=models.CharField(primary_key=True,max_length=10)
    name=models.CharField(max_length=40)
    referred_by=models.ForeignKey(Employee,on_delete=models.CASCADE,to_field="empid")
    email=models.EmailField(max_length=50)
    invitation_sent=models.BooleanField(default=True)
    invitation_valid=models.BooleanField(default=True)

