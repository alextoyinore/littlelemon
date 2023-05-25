from . import models
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'émail', 'groups']

class MenuSerializer(ModelSerializer):
    class Meta:
        model = models.Menu
        fields = '__all__'

class BookingSerializer(ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'

