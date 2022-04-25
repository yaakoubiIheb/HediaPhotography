from rest_framework import serializers
from .models import*


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Theme
        fields='__all__'





class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projet
        fields='__all__'