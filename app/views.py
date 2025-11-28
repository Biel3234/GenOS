from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import OrdemServico
from .forms import OsForm

class ListOS(ListView):
    model = OrdemServico
    context_object_name = 'ordens'
    template_name = 'list_os.html'

class CreateOS(CreateView):
    model = OrdemServico
    form_class = OsForm
    context_object_name = 'ordens'    
    template_name = 'create_os.html'
    success_url = reverse_lazy('listar')

    def form_valid(self, form):
        form.instance.atendente_responsavel = self.request.user
        return super().form_valid(form)

class DetailOS(DetailView):
    model = OrdemServico
    template_name = 'os_pdf.html'
    context_object_name = 'os'

class UpdateOS(UpdateView):
    model = OrdemServico
    context_object_name = 'os'    
    template_name = 'os_pdf.html'
    success_url = reverse_lazy('listar')