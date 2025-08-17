from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
        



class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text='Separate tags with commas'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['tags'] = ', '.join(
                tag.name for tag in self.instance.tags.all()
            )

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            
            # Handle tags
            tag_names = [name.strip() for name in self.cleaned_data['tags'].split(',') if name.strip()]
            tags = []
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name.lower())
                tags.append(tag)
            post.tags.set(tags)
            
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...'
            })
        }