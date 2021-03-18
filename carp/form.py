from django import forms
from .models import book, activity, notification, album

class bookForm(forms.ModelForm):
    class Meta:
        model= book
        fields= '__all__'

class activityForm(forms.ModelForm):
    class Meta:
        model= activity
        fields= '__all__'


class notificationForm(forms.ModelForm):
    class Meta:
        model= notification
        fields= '__all__'
class albumForm(forms.ModelForm):
    class Meta:
        model= album
        fields= '__all__'
