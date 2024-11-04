from django.shortcuts import render

# Create your views here.
#aqui hay que "diseñar" las páginas
#y luego en urls.py hay que añadirle dirección a cada pagina
def index(request):
    return render(request, 'appPromoConcert/index.html')
