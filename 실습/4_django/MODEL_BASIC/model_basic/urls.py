# master urls~~~

from django.contrib import admin
from django.urls import path, include   # include는 forward의 의미

urlpatterns = [
    path('admin/', admin.site.urls),     # 장고는 앞에 / 쓰지 않고 뒤에서만 사용
    path('board/', include('board.urls')),
    path('articles/', include('articles.urls'))
]
