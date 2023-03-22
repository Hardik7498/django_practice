from django.contrib import admin
from .models import User

@admin.register(User)
class User(admin.ModelAdmin):
    list_display=["User_Id","User_Name","User_Email","User_Designation","User_city"]
