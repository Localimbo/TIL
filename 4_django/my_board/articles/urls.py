from django.urls import path
from . import views

app_name = "articles"          # 구분 쉽도록 app name 따로 설정.

urlpatterns = [
    # Read
    path('', views.index, name="index"),  # 전체 리스트 보여짐
    path('<int:article_id>/', views.detail, name='detail'),

    # Create
    # path('new/', views.new, name='new'),  # 새로운 글 생성 하는 비어있는 form 보여짐
    path('create/', views.create, name="create"),  # 해당 게시물을 저장, name을 또 따로 주는 이유? 변경시에 한번에 바꿀 수 있도록 변수처럼 설정

    # Delete
    path('<int:article_id>/delete/', views.delete, name="delete"),

    # Update
    # path('<int:article_id>/edit/', views.edit, name="edit"),  # 수정하기 위한 form 보여짐
    path('<int:article_id>/update/', views.update, name="update"),  # 수정한 결과 저장
]