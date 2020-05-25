from django.shortcuts import render, HttpResponse

# Create your views here.
from core.models import Evento


def eventos(request, titulo_evento):
    evento=Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)


def listaeventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos':evento,}
    return render(request, 'agenda.html', dados)


# def index(request):
#     return redirect('/agendas/')