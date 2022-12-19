from django import forms
from .models import UserInput

class InputForm(forms.ModelForm):
    
    class Meta:
        model = UserInput
        fields = "__all__"
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'x-axis label...'}),
            'num_of_items': forms.TextInput(attrs={'class': 'form-control','placeholder':'amount...'},)
        }
    