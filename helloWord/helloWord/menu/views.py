from django.shortcuts import render
from .models import Principal

def index(request):
    lista_principais = Principal.objects.order_by('descricao_text')[:5]
    context = {'lista_principais': lista_principais}
    return render(request, 'menu/index.html', context)