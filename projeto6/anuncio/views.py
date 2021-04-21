from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Categoria
from .models import Anuncio

def home(request):
  categorias = Categoria.objects.all()
  anuncios = Anuncio.objects.all()[:12]
  return render(request, 'home.html', {'categorias': categorias,
                                       'anuncios': anuncios})