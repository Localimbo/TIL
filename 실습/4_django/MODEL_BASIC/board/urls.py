from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new_article),  # /board/new/
    path('create/', views.create_article), # /board/create/

    # Read
    path('', views.article_list), # /board/
    path('<int:article_id>/', views.article_detail),    # /board/2/

# 하나하나를 실제로 수정 혹은 업로드 해야 하기 때문에 id값이 꼭 필요하다.
    # Update
    path('<int:article_id>/edit/', views.edit_article),  # /board/edit
    path('<int:article_id>/update/', views.update_article),  # /board/update

    # Delete
    path('<int:article_id>/delete/', views.delete_article),  #/board/1/delete
]