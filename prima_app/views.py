from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("<h1>Ciao a tutti! Benvenuti nella homepage!</h1>")