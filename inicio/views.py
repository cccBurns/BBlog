
from django.shortcuts import render
from .models import Foto

def foto_list(request):
    fotos = Foto.objects.all()
    return render(request, 'inicio/foto_list.html', {'fotos': fotos})