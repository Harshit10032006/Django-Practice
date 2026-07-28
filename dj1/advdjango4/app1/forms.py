from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image # not just an Variable but to tell django that this form is for the Image model
        fields = ['title', 'image']