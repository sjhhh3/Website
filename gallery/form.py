from django import forms
from .models import PhotoComment

class CommentCreate(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['author', 'body']