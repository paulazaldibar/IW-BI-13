from django.shortcuts import render, get_object_or_404
from .models import PromotorMusical, Festival, Interprete
from django.db.models import OuterRef,Subquery,Max

# Create your views here.
#aqui hay que "diseñar" las páginas
#y luego en urls.py hay que añadirle dirección a cada pagina

def main(request):
    return render(request, 'appPromoConcert/main.html')


#home
def index(request):

    subconsulta = Festival.objects.filter(promotor=OuterRef('promotor')).order_by('-fecha_inicio').values('id')[:1]

    # Obtener un festival por cada promotor (el más reciente como ejemplo)
    festivales_por_promotor = Festival.objects.filter(id__in=Subquery(subconsulta))

    for festival in festivales_por_promotor:
        festival.imagen_url = f'img/festivales/{festival.id}.png'


    return render(request, 'appPromoConcert/index.html', {
        'festivales': festivales_por_promotor,
    })


#promotores
def about(request):
    promotores = PromotorMusical.objects.all()
    return render(request, 'appPromoConcert/about.html', {'promotores' : promotores})

def promotor_detalle(request, promotor_id):
    promotor = get_object_or_404(PromotorMusical, pk=promotor_id)
    festivales = promotor.festivales.all()
    return render(request, 'appPromoConcert/promotor_detalle.html', {'promotor':promotor, 'festivales': festivales})

#festivales
def track(request):
    festivales = Festival.objects.all()
    
    context = {
        'festivales': festivales,
    }
    return render(request, 'appPromoConcert/track.html', context)

def festival_detalle(request, id):
    festival = get_object_or_404(Festival, id=id)
    interpretes = festival.interpretes.all()
    return render(request, 'appPromoConcert/festival_detalle.html', {'festival': festival, 'interpretes': interpretes})



def test_base(request):
    return render(request, 'base.html')


#interpretes
def contact(request):
    interpretes = Interprete.objects.all()
    return render(request, 'appPromoConcert/contact.html', {'interpretes': interpretes})

def interprete_detalle(request, id):
    interprete = get_object_or_404(Interprete, id=id)  
    return render(request, 'appPromoConcert/interprete_detalle.html', {'interprete': interprete})
