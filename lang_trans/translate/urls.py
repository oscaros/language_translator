
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homePage, name='home_page'),
    # path('translateText/$', views.translateText, name='translateText'),
    path('how-it-works/', views.howItWorksPage, name='how_it_works'),
    re_path(r'^autoDetectText/$', views.autoDetectText, name='autodetecttext'),
    re_path(r'^translateText/$', views.translateText, name='translatetext'),
]
