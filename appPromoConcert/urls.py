from django.urls import path
#from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    MainView, IndexView, AboutView, PromotorDetalleView, TrackView,
    NuevaReseñaView, ContactView, InterpreteDetalleView, 
    FestivalDetalleView, ReseñasView, ContactView, TestBaseView
)



#urlpatterns = [
#    path('', views.index, name='index'),
#    path('about/', views.about, name='about'),
#    path('promotor/<int:promotor_id>/', views.promotor_detalle, name='promotor_detalle'),
#
#    path('contact/',views.contact, name='contact'),
#    path('interprete/<int:id>/', views.interprete_detalle, name='interprete_detalle'), 


#    path('track/',views.track, name='track'),
#    path('track/<int:id>/', views.festival_detalle, name='festival_detalle'),
    
#    path('main/',views.main, name='main'),
#    path('base/', views.test_base, name='test_base'),

#    path('reseñas/', views.reseñas, name='reseñas'),
#    path('reseñas/nueva/', views.nueva_reseña, name='nueva_reseña'),

#]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('promotor/<int:pk>/', PromotorDetalleView.as_view(), name='promotor_detalle'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('interprete/<int:pk>/', InterpreteDetalleView.as_view(), name='interprete_detalle'), 
    path('track/', TrackView.as_view(), name='track'),
    path('track/<int:pk>/', FestivalDetalleView.as_view(), name='festival_detalle'),
    path('main/', MainView.as_view(), name='main'),
    path('base/', TestBaseView.as_view(), name='test_base'),
    #path('track/<int:pk>/', FestivalDetalleView.as_view(), name='festival_detalle'), 
    path('reseñas/', ReseñasView.as_view(), name='reseñas'),
    path('reseñas/nueva/', NuevaReseñaView.as_view(), name='nueva_reseña'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

