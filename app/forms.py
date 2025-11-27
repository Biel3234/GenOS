from .models import OrdemServico
from django import forms

class OsForm(forms.ModelForm):
    class Meta():
        model = OrdemServico

        fields = [
            'cliente','telefone','moto','placa','problema_relatado','servico_executado','mecanico_responsavel','valor_total'
            ]
        

        labels = {
            'cliente': 'Nome do cliente:',
            'telefone': 'Telefone do cliente:',
            'moto': 'Moto do cliente:',
            'placa': 'Placa da moto:',
            'problema_relatado': 'Problema relatado:',
            'servico_executado': 'Serviço executado:',
            'mecanico_responsavel': 'Mecanico reponsavel:',
            'valor_total': 'Valor total:'
        }

        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'moto': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'problema_relatado': forms.Textarea(attrs={'class': 'form-control'}),
            'servico_executado': forms.Textarea(attrs={'class': 'form-control'}),
            'mecanico_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_total': forms.TextInput(attrs={'class': 'form-control'}),
        }