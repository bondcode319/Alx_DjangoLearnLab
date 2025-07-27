from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    """Form for creating and updating books"""
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'isbn', 'pages', 'cover', 'language']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter publication year'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ISBN'
            }),
            'pages': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of pages'
            }),
            'cover': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cover image URL (optional)'
            }),
            'language': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Language'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make sure authors are available in the dropdown
        self.fields['author'].queryset = Author.objects.all()
        
        # Add help text
        self.fields['isbn'].help_text = 'Enter 13-digit ISBN'
        self.fields['publication_year'].help_text = 'Year the book was published'
    
    def clean_isbn(self):
        """Validate ISBN format"""
        isbn = self.cleaned_data.get('isbn')
        if isbn and len(isbn) != 13:
            raise forms.ValidationError('ISBN must be exactly 13 characters long')
        return isbn
    
    def clean_publication_year(self):
        """Validate publication year"""
        year = self.cleaned_data.get('publication_year')
        if year and (year < 1000 or year > 2024):
            raise forms.ValidationError('Please enter a valid publication year')
        return year