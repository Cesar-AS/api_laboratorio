from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def gerar_dados_view(request, *args, **kwargs):
    return render(request, "gerar_dados.html", {})