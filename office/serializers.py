from rest_framework import serializers
from .models import CityModel, OfficeModel


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeModel
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'