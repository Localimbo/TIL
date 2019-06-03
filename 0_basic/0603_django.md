# 0603 장고



## 설치

```python
# 장고 올바른 버전으로 설치
$ pip install django==2.1.8

# 파일 위치 변경
$ cd 4_django/

# 알아서 디폴트 파일 생성 해주는, 장고 시작 할 때 쓰는 첫번째 명령어 
$ django-admin startproject first_django

# home이라는 이름을 가진 앱 추가 생성 
$ django-admin startapp home

# 실행 
$ python manage.py runserver
```

## 

## 장고?

[프로젝트 루트] 
= app1, app2, app3를 더한 것 

각각의 app 들이 모여서 한 플젝을 이룬다.

[부르는 이름] 
'FIRST_DJANGO' > 프로젝트
자동으로 생성 된 'first_django' > 마스터 앱 