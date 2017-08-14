from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('author', 'text')
    widgets = {
      'author': forms.TextInput(attrs={'class': 'form-control'}),
      'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    }