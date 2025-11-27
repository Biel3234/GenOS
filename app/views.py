from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.shortcuts import render

from .models import OrdemServico
from .forms import OsForm

class ListOS(ListView):
    model = OrdemServico
    context_object_name = 'os'
    template_name = 'list_os.html'

