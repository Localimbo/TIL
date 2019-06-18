from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # user를 create할 폼!
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .models import User

# 회원가입, Create 로직이랑 동일
def signup(request):
    if request.user.is_authenticated: # 로그인 했다면, user야 인증되있는 상태니?
        return redirect("posts:index")    #너 로그인 했으니까 여기 안보여줌
    if request.method == "POST":                 # 저장
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')

    else:                                        # get 방식으로 form 보여주기- 입력하게 폼 좀 줘봐
        form = CustomUserCreationForm()                # User 생성만을 위한 form
    return render(request, 'accounts/signup.html', {'form' : form})

# login
def login(request):
    if request.user.is_authenticated: # 로그인 했다면, user야 인증되있는 상태니?
        return redirect("posts:index")    #너 로그인 했으니까 여기 안보여줌
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)    # 해당 form은 request도 앞에 붙혀줘야 함. 그냥 문법이 다른거
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')

    else:
        form = AuthenticationForm()            # 알맞게 id, pw 입력하였는지 인증하는 폼
    return render(request, 'accounts/login.html', {'form':form})

# logout
def logout(request):
    auth_logout(request)
    return redirect('posts:index')

# user_page
# 나=user와 내가 보고 있는 사람 user_info 구분
def user_page(request, user_id):
    user_info = User.objects.get(id=user_id)
    context = {
        'user_info': user_info
    }
    return render(request, 'accounts/user_page.html', context)

# follow
def follow(request, user_id):
    me = request.user   # 로그인한 사람 변수
    you = User.objects.get(id=user_id)   # 찾을 사람 변수

    if me != you :                      # 로그인한 사람, 찾을 사람이 다르다면, ㄱㄱㄱ
        # if you in me.follow.all():      # 팔로우 했으면
        #     me.follow.remove(you)       # 팔로우 취소
        # else:                           # 팔로우 안했으면
        #     me.follow.add(you)          # 팔로우 추가
        if me in you.follower.all():     # 너를 팔로우 하는 사람들 목록에 내가 있으면
            you.follower.remove(me)      # 팔로우 취소
        else :                           # 있으면
            you.follower.add(me)         # 팔로우 추가

    return redirect('accounts:user_page', user_id)

