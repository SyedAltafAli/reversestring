from django.urls import path
from . import views

urlpatterns = [
    path('', views.reverse_string, name='reverse_string'),
]
