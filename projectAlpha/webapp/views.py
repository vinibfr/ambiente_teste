from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>HEY, AMO VOCÊ MAIS DO QUE TUDO NO MUNDO, SUA LINDA!</h2>")