from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "primeiro_app/home.html")


def data_e_hora(request):
    now = datetime.datetime.now()
    html = f"<html><body>Data/Hora:`{now}.</body/></html>"
    return HttpResponse(html)



# Create your views here.
