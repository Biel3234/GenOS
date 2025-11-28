from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.ListOS.as_view(), name='listar'),
    path('criar/', views.CreateOS.as_view(), name='criar'),
    path('atualizar/<int:pk>/', views.UpdateOS.as_view(), name='atualizar'),
    path('detalhar/<int:pk>/', views.DetailOS.as_view(), name='detalhar')
]