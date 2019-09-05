from django.shortcuts import render, HttpResponse



def index(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')    #원래는 templates/home/경로지만 templates는 안써도 인식 자동

def help_me(request):
    return render(request, 'home/help_me.html')


