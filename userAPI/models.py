from django.db import models


class User(models.Model):
    User_Id = models.AutoField(primary_key=True)
    User_Name = models.CharField(max_length=50)
    User_Email = models.EmailField(max_length=50)
    User_Designation= models.CharField(max_length=100)
    User_city = models.CharField(max_length=40)