from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.ListOS.as_view())
]