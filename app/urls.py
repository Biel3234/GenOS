from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listar/', views.ListOS.as_view(), name='listar'),
    path('criar/', views.CreateOS.as_view(), name='criar'),
    path('atualizar/<int:pk>/', views.UpdateOS.as_view(), name='atualizar'),
    path('detalhar/<int:pk>/', views.DetailOS.as_view(), name='detalhar'),
    path('pdf/<int:pk>/', views.generate_pdf, name='baixar_pdf'),
    path('deletar/<int:pk>/', views.DeleteOS.as_view(), name='deletar'),
    path('login/', views.logar, name='logar'),
    path('logout/', views.deslogar, name='deslogar'),
    path('delete/', views.DeleteOS.as_view(), name='deletar')
]