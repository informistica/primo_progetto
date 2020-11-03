from django.http import HttpResponse
from .models import Articolo, Giornalista
# Create your views here.

def home(request):
     a = []
     g = []
     for art in Articolo.objects.all():
         a.append(art.titolo)

     for gio in Giornalista.objects.all():
         g.append(gio.nome)

     response = str(a) + "<br>" + str(g)
     print(response)

     return HttpResponse("<h1>" + response + "</h1>")
