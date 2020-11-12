from django.urls import path,include
from . import views
from price import urls


urlpatterns = [
    path('', views.service, name='service'),
    path('<str:name>/price', include(urls) , name='price')
]