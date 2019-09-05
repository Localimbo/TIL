from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, HashTag
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.http import JsonResponse

@login_required
def index(request):
    user_follow = request.user.follow.all()   # 지금 로그인 한 사람이 현재 팔로우하고 있는 사람들의 전체 리스트
    follow_list = chain(user_follow, [request.user])    # 두 가지 정보를 연결시켜 저장
    posts = Post.objects.order_by('-id').filter(user__in=follow_list) # 팔로우 한 사람만 보기
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form
    }
    return render(request, 'posts/index.html', context)


def all (request):
    posts = Post.objects.all().order_by('-id')  # id 값 역순으로 정렬할꺼야~~ (-content) 도 가능!
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form
    }
    return render(request, 'posts/index.html', context)


@login_required()
def create(request):
    # 1. get 방식으로 데이터를 입력 할 수 있는 form을 요청한다.
    # 4. 사용자가 데이터를 입력해서 post 요청을 보낸다.
    # 9. 사용자가 적절한 데이터를 입력해서 post 요청을 보낸다
    if request.method == "POST":
        # 5. post 방식으로 저장요청을 받고, 데이터를 받아서 PostForm을 인스턴스화 한다.
        # 10. 데이터를 받아서 PostForm을 인스턴스화 한다.
        form = PostForm(request.POST, request.FILES)  # 이미지 파일은 POST가 아닌 Files에 저장
        # 6. 데이터 검증을 한다.
        # 11. 데이터 검증을 한다.
        if form.is_valid():
            # 12. 적절한 데이터가 들어온다. 저장 하고 인덱스로 보낸다.
            # commit 을 False라고 하는 것은 아직 저장하지말고 기다려. git 에서 add한 이후 commit 하는 작업과 같이, 아직 유저 정보를 넣지 않았기 때문에! 데이터 칼럼을 채운 이후에 저장을 한다
            post = form.save(commit=False)
            post.user = request.user
            post.save()     # 저장이 된 후에 id값이 생성되면, post와 hashtag 연결 가능해진다.

            # hashtag 추가
            content = form.cleaned_data.get('content')    # cleaned_data : 살짝 다듬어진 데이터
            words = content.split()
            for word in words:
                if word[0] == "#":
                    # 해시태그 생성
                    hashtag = HashTag.objects.get_or_create(content=word)  #이미 있을수도 있으니 생성하거나, 가져오기
                    # post 모델과 연결
                    post.hashtags.add(hashtag[0])
            return redirect("posts:index")
        else:
            # 7. 적절하지 않은 데이터가 들어온다.
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

@login_required()
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.user:
        # 내가 작성한 글일때
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()

                # 기존의 N:N 관계를 삭제
                post.hashtags.clear()
                # hashtag 추가
                content = form.cleaned_data.get('content')  # cleaned_data : 살짝 다듬어진 데이터
                words = content.split()
                for word in words:
                    if word[0] == "#":
                        # 해시태그 생성
                        hashtag = HashTag.objects.get_or_create(content=word)  # 이미 있을수도 있으니 생성하거나, 가져오기
                        # post 모델과 연결
                        post.hashtags.add(hashtag[0])


                return redirect("posts:index")
            else:
                pass
        else:
            form = PostForm(instance=post)
        return render(request, 'posts/form.html', {'form': form})
    else:
        # 내가 작성하지 않은 글일때
        return redirect("posts:index")


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:index')

@login_required()
def comment_create(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('posts:index')

@login_required()
def likes(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)

    # 이미 좋아요가 눌려졌으면
    if user in post.like_users.all():      # 지금 로그인 한 사람이 like_users 컬럼에 속해있는지?
        # 좋아요 취소
        post.like_users.remove(user)
        is_like = False
    # 좋아요 안했다면
    else:
        # 좋아요 추가
        post.like_users.add(user)
        is_like = True
    context= {
        'is_like' : is_like
    }
    return JsonResponse(context)
    # return redirect("posts:index")
\

def hashtags(request, hashtag_id):               # all과 구조 거의 똑같음
    hashtag = HashTag.objects.get(id=hashtag_id)
    posts = hashtag.post_set.all() # 해쉬태그가 포함되어 있는 모든 게시물 리스트 가져오기 _set 사용
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
        'hashtag' : hashtag,
    }
    return render(request, 'posts/index.html', context)


def javascript(request):

    return render(request, 'posts/js.html')