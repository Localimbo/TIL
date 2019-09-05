from django.shortcuts import render, redirect
from .models import Article, Comment

# read 요청

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


# create 요청

# def new(request):
#     return render(request, 'articles/new.html')

# RESTFUL, 하나의 url이지만 보내는 방식(Get/Post)에 따라 다르게 처리
def create(request):
    if request.method == "POST":                 # form 저장하기
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.user = request.user
        article.save()
        return redirect('articles:detail', article.id)
    else:                                        # 새로운 글 생성하는 form 보여줌.
        return render(request, 'articles/form.html')

# delete 요청

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')

# Update 요청

# def edit(request, article_id):
#     article = Article.objects.get(id=article_id)
#     context = {
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)   #render = python 작성을 html로 변환해주는 역할

def update(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(id=article_id)        # 수정한 결과 저장!  id값이 ~인거 찾아줭
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.id)
    else:
        article = Article.objects.get(id=article_id)         # 수정하기 위한 form 보여짐
        context = {
            'article': article
        }
        return render(request, 'articles/form.html', context)


# comment는 article에 속해 있어야만 한다. article_id 인자 가져와야 함
def comment_create(request, article_id):
    comment = Comment()
    article = Article.objects.get(id=article_id) # 'name'의 이름
    comment.article = article
    comment.content = request.POST.get('content')
    comment.user = request.user
    comment.save()

    return redirect("articles:detail", article_id)

# comment delete 요청
def comment_delete(request, article_id, comment_id):     # url에 함수 인자 2개 정의했기 때문에, 무조건 넣어야 함
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('articles:detail', article_id)

# comment 모두 요청
def comment_all(request):
    return render(request, 'articles/comment_all.html')