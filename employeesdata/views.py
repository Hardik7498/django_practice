from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from employeesdata.serializers import DepartmentSerializer, EmployeeSerializer
from employeesdata.models import Departments, Employees


class EmployeeAPI(ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class Employee_API(RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentAPI(ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


class Department_API(RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
