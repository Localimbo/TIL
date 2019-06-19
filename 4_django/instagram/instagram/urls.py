from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.all),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # /media/와 같음. 하지만, 변수화 시킨 변수 사용하는 것이 더 편리
