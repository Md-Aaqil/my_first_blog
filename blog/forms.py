from django import forms

from .models import post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
