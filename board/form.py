from django import forms
from .models import Comment

class CommentCreate(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']