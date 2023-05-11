from django.contrib import admin
from .models import Employee,Guest

# Register your models here.
@admin.register(Employee)
class EmpAdmin(admin.ModelAdmin):
    list_display=['empid','name','email',]


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display=['guestid','name','referred_by','email','invitation_sent','invitation_valid']