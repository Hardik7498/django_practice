
from rest_framework import serializers
from userAPI.models import User



class userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('User_Id', 'User_Name', 'User_Email','User_Designation','User_city')




