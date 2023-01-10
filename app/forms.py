from django import forms
from .models import UserInput
from .validators import validate_file_extension

class InputForm(forms.ModelForm):
    
    class Meta:
        model = UserInput
        fields = "__all__"
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'x-axis label...'}),
            'num_of_items': forms.TextInput(attrs={'class': 'form-control','placeholder':'amount...'})
        }
    
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False
        self.fields['num_of_items'].required = True

class FileForm(forms.Form):

    files = forms.FileField(label='', widget=forms.FileInput(attrs={'class': 'file_form'}), validators=[validate_file_extension])