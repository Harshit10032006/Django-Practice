from rest_framework import serializers
from .models import Person, Color



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']



class PeopleSerializer(serializers.ModelSerializer):

    color= ColorSerializer()
    class Meta :
        model=Person
        fields='__all__'
        # depth=1
