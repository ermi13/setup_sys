from django.urls import path, include
from . import views
from services import urls


urlpatterns = [
    path('', views.home, name="home"),
    path('submit',views.feedback, name="submit")
]