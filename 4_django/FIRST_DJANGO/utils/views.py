from django.shortcuts import render

def index(request):
    return render(request, 'utils/index.html')

def arti(request, keyword):
    import art
    result = art.text2art(keyword, 'random')    # 'random'도 가능
    context = {
        'result' : result,
        'keyword' : keyword,
    }
    return render(request, 'utils/arti.html', context)

def stock(request):
    pass   # TODO : 완성하기

