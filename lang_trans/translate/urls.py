
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    # path('translateText/$', views.translateText, name='translateText'),
    re_path(r'^autoDetectText/$', views.autoDetectText, name='autodetecttext'),
    re_path(r'^translateText/$', views.translateText, name='translatetext'),
]
