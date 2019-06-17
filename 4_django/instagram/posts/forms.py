from django import forms
from .models import Post, Comment

# 폼을 만들어주는 친구 ^^
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']