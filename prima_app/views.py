from django.http import HttpResponse
# Create your views here.

#L1
def homepage(request):
    return HttpResponse("<h1>Ciao a tutti! Benvenuti nella homepage!</h1>")

#L3
def menu(request):
    return HttpResponse("<ol><li>Prima opzione</li><li>Seconda opzione</li><li>Terza opzione</li></ol>")