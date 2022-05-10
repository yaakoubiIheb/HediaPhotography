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





class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'








class ViedoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'






class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personne
        fields='__all__'








class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Information
        fields='__all__'


