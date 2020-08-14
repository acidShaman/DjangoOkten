from rest_framework import serializers
from .models import AnimalModel, AnimalMonikerModel
from django.contrib.auth import get_user_model

User = get_user_model()


class AnimalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = '__all__'


class MonikerCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalMonikerModel
        fields = ['moniker']


class AnimalCustomSerializer(serializers.ModelSerializer):
    monikers = MonikerCustomSerializer(many=True)

    class Meta:
        model = AnimalModel
        fields = ['name', 'animal_type', 'monikers']


class UserDetailSerializer(serializers.ModelSerializer):
    animals = AnimalCustomSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'animals']
