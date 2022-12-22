from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect
from .models import Livro
from .form import LivroForm


def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "primeiro_app/home.html")

def listagem(request):
    dados = {"livros": Livro.objects.all()}
    return render(request, "primeiro_app/listagem.html", dados)


def data_e_hora(request):
    now = datetime.datetime.now()
    html = f"<html><body>Data/Hora:`{now}.</body/></html>"
    return HttpResponse(html)


def criar(request):
    dados = {}
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    dados["form"] = form
    dados["Livro"] = Livro
    return render(request, "primeiro_app/form.html", dados)


def update(request, pk):
    dados = {}
    livro = Livro.objects.get(pk=pk)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    dados["form"] = form
    dados["livro"] = livro
    return render(request, "primeiro_app/form.html", dados)

def delete(request, pk):
    livro = Livro.object.get(pk=pk)
    livro.delete()
    return redirect("url_listagem")
# Create your views here.
