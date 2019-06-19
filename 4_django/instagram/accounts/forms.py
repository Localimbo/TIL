from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)        # customize 가능. 칼럼 추가를 원하면 필드에 추가 ㄱ


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('email', 'introduce', 'image',)