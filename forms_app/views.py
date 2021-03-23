from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import FormContatto, FormRegistrazione
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def contatti(request):

    # Se la richiesta è di tipo POST, allora possiamo processare i dati
    if request.method == "POST":
        # Creiamo l'istanza del form e la popoliamo con i dati della POST request (processo di "binding")
        form = FormContatto(request.POST)
        # is_valid() controlla se il form inserito è valido:
        if form.is_valid():
            # a questo punto possiamo usare i dati validi!
            # tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di Python
            print("Il Form è Valido!")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("EMAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)
            # ringrazio l'utente per averci contattato - volendo possiamo effettuare un redirect a una pagina specifica
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
    # Se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form = FormContatto()
    # arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta(con metodo GET), o se il form non è valido e ha errori
    context = {"form": form}
    return render(request, "contatto.html", context)


def registrazioneView(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]   #fai attenzione all' 1
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)  #si controllano le credenziali
            login(request, user)  # si effettua il login per l'utente autenticato
            return HttpResponseRedirect("/")
    else:  # se la richiesta è di tipo GET viene mostrato il form vuoto (unbounded)
        form = FormRegistrazione()
    context = {"form": form}
    return render(request, 'registrazione.html', context)





