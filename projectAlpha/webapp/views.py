from django.shortcuts import render

def index(request):
    return render(request, 'webapp/home.html')

def contact(request):
    return render(request, 'webapp/contact.html')    
