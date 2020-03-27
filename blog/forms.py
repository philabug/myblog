from django.contrib.auth.models import User
from .models import Blog
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
    
    def clean_author(self):
        if not self.cleaned_data['author']:
            return User()
        return self.cleaned_data['author']
