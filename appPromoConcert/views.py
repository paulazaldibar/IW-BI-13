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

def elements(request):
    # Definir las rutas de las imágenes
    image1 = 'img/elements/g1.jpg'
    image2 = 'img/elements/g2.jpg'
    image3 = 'img/elements/g3.jpg'
    image4 = 'img/elements/g4.jpg'
    image5 = 'img/elements/g5.jpg'
    image6 = 'img/elements/g6.jpg'
    image7 = 'img/elements/g7.jpg'
    image8 = 'img/elements/g8.jpg'

    # Pasarlas al contexto
    context = {
        'image1': image1,
        'image2': image2,
        'image3': image3,
        'image4': image4,
        'image5': image5,
        'image6': image6,
        'image7': image7,
        'image8': image8,
    }

    return render(request, 'appPromoConcert/elements.html', context)
