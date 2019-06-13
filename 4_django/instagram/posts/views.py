from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)

def create(request):
    # 1. get 방식으로 데이터를 입력 할 수 있는 form을 요청한다.
    # 4. 사용자가 데이터를 입력해서 post 요청을 보낸다.
    # 9. 사용자가 적절한 데이터를 입력해서 post 요청을 보낸다
    if request.method == "POST":
        # 5. post 방식으로 저장요청을 받고, 데이터를 받아서 PostForm을 인스턴스화 한다.
        # 10. 데이터를 받아서 PostForm을 인스턴스화 한다.
        form = PostForm(request.POST)
        # 6. 데이터 검증을 한다.
        # 11. 데이터 검증을 한다.
        if form.is_valid():
            # 12. 적절한 데이터가 들어온다. 저장 하고 인덱스로 보낸다.
            form.save()
            return redirect("posts:index")
        else:
            # 7. 적잘하지 않은 데이터가 들어온다.
            pass

    else:
        # 2. PostForm을 인스턴스화 해서 form 변수에 저장 ! 자동완성 시켜서 보내줄게~
        form = PostForm()     # form 변수 context 변수에 담아서 보냄

    context = {
        'form': form
    }
    # 3. 만들어진 form을 create.html에 담아서 전송
    # 8. 사용자가 정확하게 입력한 데이터를 유지한 상태의 form을 전송
    return render(request, 'posts/form.html', context)

def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:index")
        else:
            pass
    else:
        # 기존에 작성된 폼 보여주기 !
        form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'form':form})

def delete(request, post_id):
