from django.urls import path
from employeesdata import views



urlpatterns = [
    path('department/', views.DepartmentAPI),
    path('employee/', views.EmployeeAPI),
   
]
