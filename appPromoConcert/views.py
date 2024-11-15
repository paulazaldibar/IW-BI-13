from django.shortcuts import render

# Create your views here.
#aqui hay que "diseñar" las páginas
#y luego en urls.py hay que añadirle dirección a cada pagina
def index(request):
    return render(request, 'appPromoConcert/index.html')

def about(request):
    return render(request, 'appPromoConcert/about.html')
def blog(request):
    return render(request, 'appPromoConcert/blog.html')
def contact(request):
    return render(request, 'appPromoConcert/contact.html')
def elements(request):
    return render(request, 'appPromoConcert/elements.html')
def main(request):
    return render(request, 'appPromoConcert/main.html')
def single_blog(request):
    return render(request, 'appPromoConcert/single-blog.html')
def track(request):
    return render(request, 'appPromoConcert/track.html')
