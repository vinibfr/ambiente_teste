from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['Se quiser falar comigo, tentae pelo e-mail:','vinibfr@gmail.com']})    
