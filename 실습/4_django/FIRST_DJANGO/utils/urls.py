from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                      #utils/ 라는 패턴을 의미.
    path('art/<str:keyword>/', views.arti),     #utils/art/<keyword>
    path('stock_input/', views.stock_input),    # utils/stock_input/
    path('stock_output/', views.stock_output),  # utils/stock_output/e

]