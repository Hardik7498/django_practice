from django.contrib import admin
from django.urls import path
from userAPI import views

lookup_field='pk'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userdata/', views.UserAPI.as_view()),
    path('modifyuserdata/<int:pk>/', views.User_API.as_view()),
]
