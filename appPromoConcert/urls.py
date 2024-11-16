from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('promotor/<int:promotor_id>/', views.promotor_detalle, name='promotor_detalle'),

    path('contact/',views.contact, name='contact'),
    path('interprete/<int:id>/', views.interprete_detalle, name='interprete_detalle'), 


    path('track/',views.track, name='track'),
    path('track/<int:id>/', views.festival_detalle, name='festival_detalle'),
    
    path('main/',views.main, name='main'),
    path('base/', views.test_base, name='test_base'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)