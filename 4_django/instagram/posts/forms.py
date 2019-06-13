from django import forms
from .models import Post

# 폼을 만들어주는 친구 ^^
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
