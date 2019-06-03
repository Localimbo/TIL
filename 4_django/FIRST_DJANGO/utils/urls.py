from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                   #utils/ 라는 패턴을 의미.
    path('art/<str:keyword>/', views.arti),   #utils/art/<keyword>
    path('stock/', views.stock),              # utils/stock/

]