from django.urls import path
from . import views


urlpatterns = [
    path('', views.url_shortener, name='urlShort'),
    path('<str:slugs>', views.url_redirect, name='redirect')
]
