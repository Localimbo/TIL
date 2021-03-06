# 0603 장고



## 장고 

[프로젝트 루트] 
= app1, app2, app3를 더한 것 

각각의 app 들이 모여서 한 플젝을 이룬다.

[부르는 이름] 
'FIRST_DJANGO' > 프로젝트
자동으로 생성 된 'first_django' > 마스터 앱 



## 설치 및 세팅

```python
# 장고 올바른 버전으로 설치
$ pip install django==2.1.8

# 파일 위치 변경
$ cd 4_django/

# 알아서 디폴트 파일 생성 해주는, 장고 시작 할 때 쓰는 첫번째 명령어 
$ django-admin startproject first_django

# home이라는 이름을 가진 앱 추가 생성 
$ django-admin startapp home

# 만들어진 프로젝트의 setting.py 설정
# installed apps에 추가 
INSTALLED_APPS = [
    'django_extensions',     # 이런건 주로 위로 올림 
 	##########
    'board',                 # 새로 추가된 app   
]

# 변경하는거 추천~
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_TZ = False

# 실행 
$ python manage.py runserver
```



## 추가 패키지 활용 (0604)

```python
# extension, ipython, ipython[notebook] 설치 
$ pip install django-extensions ipython ipython[notebook]
```



## DATABASE

###  <파이썬으로 DB 생성하는 삼단계>

```python
# 첨으로 models.py 활용 시작

1. models.py에서 rough 하게 만듬.  # 이것만 해도 상관은 ㄴㄴ

2. # app 밑, migration 폴더 하위에 생성; 초벌번역해준다.
$ python manage.py makemigrations board

3. # board 앱에 있는 모든 mirgration이 적용됨; 결제서류 get!
$ python manage.py migrate board 
```

: DB 내, board 안에 table 생성 완료  

** Model 단계에서 초기에 표 설계, 저장할 테이블 구성이 매우 중요. 



### Sqllite viewer 에서 확인 

#### open해서 table 생성된 지 확인 

* 데이터베이스 열기 > TIL > django > db.sql3  



### Shell 사용

```sh
# 장고 세상에 들어감 
$ python manage.py shell

# import
from board.models import Article

# 객체 생성
a = Article()

# 입력
a.title = 'hi'
a.content = 'HiHi'

# 저장 + 업로드
a.save()

# 두번째 행 추가 
a2 = Article()

a2.title = 'Bye'

# shell 빠져 나오기 
ctrl+d

# shell_plus 열기
$ python manage.py shell_plus

# 전체조회
Article.objects.all() 

# id가 1인것만 가져오기
Article.objects.get(id=1) 

# 저장을 위한 노트북 켜기 
$ python manage.py shell_plus --notebook

```



## CRUD Basic  (디테일은 쥬 노트북에)

### CRUD 
* Create => 데이터 생성
* Read(Retrieve) => 데이터 조회 
* Update => 데이터 수정
* Delete => 데이터 삭제 

### Articles Table

| Field  Name                   | Data type |
| ----------------------------- | --------- |
| `id` | Interger, Primary Keu |
| `title` | CharField(max_length ==200) |
| `content` | TextField() |



## 장고 관리자 페이지 & 사용자관리

```python
from django.contrib import admin
from . models import Article

# Register your models here.
admin.site.register(Article)

1. python manage.py migrate => 모든 숨겨진 결재를 실행 
2. python manage.py createsuperuser => 절대관리자를 생성
3. DOMAIN/admin에 접속 
4. Login

```



## 모델의 클래스 수정시, migration 작업 재실행 

```python
# models.py 폴더
$ python manage.py makemigrations
$ python manage.py migrate

# admin.py 폴더
from .models import Article, Comment
admin.site.register(Comment)
```



## forms.py 생성 

```python
model 알려주면 html 코드 자동으로 생성해줌
model만 수정하면 형태는 장고가 알아서 변형해주는 것

단점 : 비주얼 테러 

html에서 <form> tag, <input> 제출 버튼 달아줘야 함 
```





## django bootstrap4 설치

```python
$ pip install django-bootstrap4

settings.py INSTALLED_APPS에 
 'bootstrap4',
]
추가
```



pip install django-bootstrap4

