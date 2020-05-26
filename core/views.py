from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from core.models import Evento


def eventos(request, titulo_evento):
    evento=Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)


def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
        else:
            messages.error(request, "Usuário ou senha inválido.")
    return redirect('/')



@login_required(login_url='/login/')
def listaeventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento,}
    return render(request, 'agenda.html', dados)


# def index(request):
#     return redirect('/agendas/')
@login_required(login_url="/login/")
def evento(request):
    return render(request, "evento.html")

@login_required(login_url="/login/")
def submit_evento(request):
    if request.POST:
        usuario = request.user
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect("/")



