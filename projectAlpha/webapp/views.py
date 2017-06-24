from django.shortcuts import render

def index(request):
    return render(request, 'webapp/home.html')

def contact(request):
    return render(request, 'webapp/basic.html', {'content':['Se quiser falar comigo, tentae pelo e-mail:','vinibfr@gmail.com']})    
