from django.shortcuts import render, HttpResponse    # 문자열로 print가 불가능하기 때문에, import 해준다.


def index(request):   # 함수 쓸 때, 실행되게 하는 action의 첫 번째 인자느 무조건 request이다
    return render(request, 'index.html')

def hello(request, name):
    greeting = f'Hello, {name}'
    return render(request, 'hello.html', {'greet': greeting})  # 추가적 정보인'greeting',장고에서는 딕셔너리로 형태로 넘김
