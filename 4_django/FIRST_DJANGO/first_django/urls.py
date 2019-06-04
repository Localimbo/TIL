# 얘는 <마스터 url> 기억기억 ~~~
# 자잘한 애들은 건들이지 않고 정확하게 어느 하위 url로 보낼지를 지정해주는 것.
from django.contrib import admin
from django.urls import path, include

# ~~님 여기로 가세요~!  이 역할 만 함.
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', views.index),    # 해당 도메인에 들어오면은, views 파일에서 index 함수를 실행한다.
    #path('hello/<str:name>', views.hello),
    path('home/', include('home.urls')),    # home app의 url로 보내라! home의 url로 포워딩 하는 것! 얘가 담당함
    path('utils/', include('utils.urls')),
]
