from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from userAPI.models import User
from userAPI.serializers import userserializers
from rest_framework.mixins import UpdateModelMixin

lookup_field='pk'

class UserAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userserializers

class User_API(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userserializers
