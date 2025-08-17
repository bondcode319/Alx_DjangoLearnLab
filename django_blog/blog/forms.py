from django import forms
from django.contrib.auth.models import User
from .models import Post


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
        



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }