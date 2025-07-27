from django import forms
from .models import Book

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        data = self.cleaned_data['name']
        if 'admin' in data.lower():
            raise forms.ValidationError("Name cannot contain 'admin'")
        return data
