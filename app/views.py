from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render

from .models import OrdemServico
from .forms import OsForm

from weasyprint import HTML

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

    def generate_pdf(request, pk):
        os = OrdemServico.objects.all()
        html = render_to_string('os_pdf.html', {"os": os})

        pdf = HTML(string=html).write_pdf()

        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = "inline; filename=os.pdf"

        return response