from django.shortcuts import render, redirect
from .models import Article

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


