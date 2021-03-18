from rest_framework import serializers
from .models import book, activity, notification, album

class Book(serializers.ModelSerializer):
    class Meta:
        model= book
        fields= '__all__'

class Activity(serializers.ModelSerializer):
    class Meta:
        model=activity
        fields= '__all__'


class Notification(serializers.ModelSerializer):
    class Meta:
        model= notification
        fields= '__all__'    

class Album(serializers.ModelSerializer):
    class Meta:
        model= album
        fields= '__all__'      