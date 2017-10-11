from django import forms
from .models import BlogComment

class CommentCreate(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['author', 'body']