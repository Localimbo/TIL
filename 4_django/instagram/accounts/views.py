from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # user를 create할 폼!
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# 회원가입, Create 로직이랑 동일
def signup(request):
    if request.user.is_authenticated: # 로그인 했다면, user야 인증되있는 상태니?
        return redirect("posts:index")    #너 로그인 했으니까 여기 안보여줌
    if request.method == "POST":                 # 저장
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')

    else:                                        # get 방식으로 form 보여주기- 입력하게 폼 좀 줘봐
        form = UserCreationForm()                # User 생성만을 위한 form
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