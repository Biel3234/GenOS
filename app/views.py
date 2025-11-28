from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import OrdemServico, User
from .forms import OsForm

from weasyprint import HTML

class RequerLogin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class ListOS(RequerLogin, ListView):
    model = OrdemServico
    context_object_name = 'ordens'
    template_name = 'list_os.html'

class CreateOS(RequerLogin, CreateView):
    model = OrdemServico
    form_class = OsForm
    context_object_name = 'ordens'    
    template_name = 'create_os.html'
    success_url = reverse_lazy('listar')

    def form_valid(self, form):
        form.instance.atendente_responsavel = self.request.user
        return super().form_valid(form)

class DetailOS(RequerLogin, DetailView):
    model = OrdemServico
    template_name = 'os_pdf.html'
    context_object_name = 'os'

class UpdateOS(RequerLogin, UpdateView):
    model = OrdemServico
    context_object_name = 'os'    
    template_name = 'os_pdf.html'
    success_url = reverse_lazy('listar')

def home(request):
    return render(request, 'home.html')

def generate_pdf(request, pk):
    os = OrdemServico.objects.get(pk = pk)
    html = render_to_string('os_pdf.html', {"os": os})

    pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f"inline; filename={os}.pdf"

    return response

def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get('nome')
        password = request.POST.get('senha')

        user = authenticate(request, username=name, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse(render(request, 'usuario_nao_existe.html'))
        

def deslogar(request):
    logout(request)
    return redirect('logar')

# def registrar(request):
#     if request.method == "GET":
#         return render(request, 'register.html')
#     else:
#         name = request.POST.get('nome')
#         password = request.POST.get('senha')

#         user = User.objects.filter(username = name, password = password)

#         if user:
#             return HttpResponse(render(request, 'usuario_ja_existe.html'))
#         else:
#             user = User.objects.create_user(username=name, password= password)
#             user.save()

#     return redirect('todo:logar')
         