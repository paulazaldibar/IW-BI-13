from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),
    path('elements/',views.elements, name='elements'),
    path('single_blog/',views.single_blog, name='single-blog'),
    path('track/',views.track, name='track'),
    path('main/',views.main, name='main'),
]