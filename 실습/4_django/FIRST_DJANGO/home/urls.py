from django.urls import path
from . import views    # 같은 위치에 있는 view 파일을 import 하겠다!

urlpatterns = [
    path('', views.index),     #/home/  home 생략해도 상관 없음
    path('contact/', views.contact),   #/home/contact/
    path('help_me/', views.help_me),    #/home/help_me/
]