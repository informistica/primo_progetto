from tournament.models import Squadre, Tornei
from django.shortcuts import render
def indexTornei(request):
    #courses=Course.objects.all()
    tornei=Tornei.objects.all()
    context={'tornei':tornei}

    squadre={}
    for torneo in tornei:
        squadre2=list(map(lambda x:x.nome.upper(),torneo.squadre.all().order_by("nome")))
        squadre[torneo.nome]=squadre2
    context['squadre']=squadre
    return render(request,"indexTornei.html",context)