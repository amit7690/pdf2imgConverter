from django import forms
from .models import InputModel, PdfModel

class InputForm(forms.ModelForm):
	class Meta:
		model = InputModel
		fields = '__all__'
		widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows': 4, 'cols': 40}),
            'pdf': forms.FileInput(attrs={'class':'form-control', 'style':'width:400px'})
        }


class PdfForm(forms.ModelForm):
	class Meta:
		model = PdfModel
		fields = '__all__'
		widgets = {
			'choose_file': forms.FileInput(attrs={'class':'form-control','id':'id_image'})
		}