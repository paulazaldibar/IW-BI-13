from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .models import PromotorMusical, Festival, Interprete, Reseña
from django.db.models import OuterRef,Subquery,Max
from .forms import ReseñaForm

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.db.models import OuterRef, Subquery
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Reseña
from .forms import ReseñaForm
#from django.utils import translation
#from django.http import HttpResponseRedirect
#from django.urls import reverse 

# Create your views here.
#aqui hay que "diseñar" las páginas
#y luego en urls.py hay que añadirle dirección a cada pagina

#MAIN-------------------------------------------------------------------------------------

#funcion:
#def main(request):
#   return render(request, 'appPromoConcert/main.html')

#clase:
class MainView(TemplateView):
    template_name = 'appPromoConcert/main.html'

#INDEX--------------------------------------------------------------------------------------

#Funcion:
#def index(request):
#
#   subconsulta = Festival.objects.filter(promotor=OuterRef('promotor')).order_by('-fecha_inicio').values('id')[:1]
#
#    # Obtener un festival por cada promotor (el más reciente como ejemplo)
#    festivales_por_promotor = Festival.objects.filter(id__in=Subquery(subconsulta))

#    for festival in festivales_por_promotor:
#        festival.imagen_url = f'img/festivales/{festival.id}.png'


#    return render(request, 'appPromoConcert/index.html', {
#        'festivales': festivales_por_promotor,
#    })

#Clase:
class IndexView(ListView):
    model = Festival
    template_name = 'appPromoConcert/index.html'
    context_object_name = 'festivales'

    def get_queryset(self):
       #coger festival más reciente por cada promotor
       subconsulta = Festival.objects.filter(promotor=OuterRef('promotor')).order_by('-fecha_inicio').values('id')[:1]
       return Festival.objects.filter(id__in=Subquery(subconsulta))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #coger cada imagen por festival
        for festival in context['festivales']:
            festival.imagen_url = f'img/festivales/{festival.id}.png'
        return context

#PROMOTORES--------------------------------------------------------------------------------------

#funcion:
#def about(request):
#    promotores = PromotorMusical.objects.all()
#    return render(request, 'appPromoConcert/about.html', {'promotores' : promotores})

#Clase:
class AboutView(ListView):
    model = PromotorMusical
    template_name = 'appPromoConcert/about.html'
    context_object_name = 'promotores'

#PROMOTOR DETALLE--------------------------------------------------------------------------------------

#funcion: 
#def promotor_detalle(request, promotor_id):
#    promotor = get_object_or_404(PromotorMusical, pk=promotor_id)
#    festivales = promotor.festivales.all()
#    return render(request, 'appPromoConcert/promotor_detalle.html', {'promotor':promotor, 'festivales': festivales})


#clase:
class PromotorDetalleView(DetailView):
    model = PromotorMusical
    template_name = 'appPromoConcert/promotor_detalle.html'
    context_object_name = 'promotor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['festivales'] = self.object.festivales.all()
        return context

#FESTIVALES--------------------------------------------------------------------------------------

#funcion:
#def track(request):
#    festivales = Festival.objects.all()
    
#    context = {
#        'festivales': festivales,
#    }
#    return render(request, 'appPromoConcert/track.html', context)

#clase:
class TrackView(ListView):
    model = Festival
    template_name = 'appPromoConcert/track.html'
    context_object_name = 'festivales'


#FESTIVAL DETALLE--------------------------------------------------------------------------------------

#funcion:
#def festival_detalle(request, id):
#    festival = get_object_or_404(Festival, id=id)
#    interpretes = festival.interpretes.all()
#    return render(request, 'appPromoConcert/festival_detalle.html', {'festival': festival, 'interpretes': interpretes})

#clase:
class FestivalDetalleView(DetailView):
    model = Festival
    template_name = 'appPromoConcert/festival_detalle.html'  # Nombre del template que mostrarás
    context_object_name = 'festival'  # Este es el nombre con el que accederás al objeto en el template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        festival = self.get_object()  # Obtén el festival actual
        context['interpretes'] = festival.interpretes.all()  # Agrega los intérpretes al contexto
        return context


#INTERPRETES--------------------------------------------------------------------------------------

#funcion:
#def contact(request):
#    interpretes = Interprete.objects.all()
#    return render(request, 'appPromoConcert/contact.html', {'interpretes': interpretes})

#clase:
class InterpreteDetalleView(DetailView):
    model = Interprete
    template_name = 'appPromoConcert/interprete_detalle.html'
    context_object_name = 'interprete'

#INTERPRETE DETALLE--------------------------------------------------------------------------------------

#funcion:
#def interprete_detalle(request, id):
#    interprete = get_object_or_404(Interprete, id=id)  
#    return render(request, 'appPromoConcert/interprete_detalle.html', {'interprete': interprete})

#clase:
class ContactView(ListView):
    model = Interprete
    template_name = 'appPromoConcert/contact.html'
    context_object_name = 'interpretes'

#BASE--------------------------------------------------------------------------------------

#funcion:
#def test_base(request):
#    return render(request, 'base.html')


#clase:
class TestBaseView(TemplateView):
    template_name = 'base.html'


#RESEÑAS----------------------------------------------------------------------------------------------

#funcion:
#def reseñas(request):
#    reseñas = Reseña.objects.all().order_by('-fecha')
#    for reseña in reseñas:
#        reseña.range_calificacion = range(reseña.calificacion)
#        reseña.range_estrellas_vacias = range(5 - reseña.calificacion)
#    return render(request, 'appPromoConcert/reseñas.html', {'reseñas': reseñas})

#clase:
class ReseñasView(ListView):
    model = Reseña
    template_name = 'appPromoConcert/reseñas.html'
    context_object_name = 'reseñas'
    ordering = ['-fecha']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadir rangos de estrellas para visualización
        for reseña in context['reseñas']:
            reseña.range_calificacion = range(reseña.calificacion)
            reseña.range_estrellas_vacias = range(5 - reseña.calificacion)
        return context

#NUEVA RESEÑA-------------------------------------------------------------------------------

#funcion:
#def nueva_reseña(request):
#    if request.method == 'POST':
#        form = ReseñaForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('reseñas')
#    else:
#        form = ReseñaForm()
#    return render(request, 'appPromoConcert/nueva_reseña.html', {'form': form})

#clase:
class NuevaReseñaView(CreateView):
    model = Reseña
    form_class = ReseñaForm
    template_name = 'appPromoConcert/nueva_reseña.html'
    success_url = reverse_lazy('reseñas')


#Traduccion

#def set_language(request):
#    user_language = request.POST.get('language', 'en') 
#    translation.activate(user_language)
#    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
#    print(f'Idioma cambiado a: {user_language}')
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) 
