from django import forms
from .models import Contato, Profile, Project, Skill

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motivo do contato'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escreva sua mensagem...'}),
        }
    
    def clean_assunto(self):
        assunto = self.cleaned_data['assunto'].strip()
        if len(assunto) <= 3:
            raise forms.ValidationError('O assunto precisa ter ao menos 4 caracteres!')
        return assunto