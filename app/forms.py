from django import forms
from .models import UserInput, FileInputModel

class InputForm(forms.ModelForm):
    
    class Meta:
        model = UserInput
        fields = "__all__"
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'label..'}),
            'num_of_items': forms.TextInput(attrs={'class': 'form-control','placeholder':'value...'})
        }

class FileForm(forms.ModelForm):

    class Meta:
        model = FileInputModel
        fields = "__all__"
        widgets = {
            'files': forms.FileInput(attrs={'class':'file_form'})
        }