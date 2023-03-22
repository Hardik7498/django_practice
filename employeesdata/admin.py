from django.contrib import admin
from .models import Departments, Employees


@admin.register(Departments)
class Departmentsadmin(admin.ModelAdmin):
 list_display = ['DepartmentId', 'DepartmentName']


@admin.register(Employees)
class Employees(admin.ModelAdmin):
 list_display = ['EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName']
