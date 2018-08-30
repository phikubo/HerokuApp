from django.forms import ModelForm, TextInput, NumberInput, ChoiceField, Textarea, Select, FileInput
from .models import venta_articulo
from django import forms
from django.contrib.auth.models import User #para registrar usuarios.
class articuloForm(ModelForm):
    class Meta:
        model= venta_articulo
        fields= ['titulo', 'precio', 'marca_carros', 'descripcion', 'foto']
        #fields = ('',)
        widgets = {'titulo': TextInput(attrs={'class':'input','placeholder':'titulo'}),
                   'precio': NumberInput(attrs={'class':'input','value':0}),
                   'marca_carros':Select(attrs={'class':'select'}),
                   'descripcion': Textarea(attrs={'class':'textarea','placeholder':'Descripción',}),
                   'foto':FileInput()}


class login_form(forms.Form):
    usuario=forms.CharField(widget=forms.TextInput())
    clave=forms.CharField(widget=forms.PasswordInput(render_value=False))

class registrar_usuario_form(forms.Form):
    usuario =   forms.CharField(widget=forms.TextInput())
    correo  =   forms.EmailField(widget=forms.TextInput())
    password_1  =  forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False))
    password_2  =  forms.CharField(label='Confirmar Password',widget=forms.PasswordInput(render_value=False))
    
    def clean_usuario(self):
        usuario=self.cleaned_data['usuario']
        try:
            usr=User.objects.get(username=usuario)
        except User.DoesNotExist:
            return usuario
        raise forms.ValidationError('Nombre de usuario ya registrado')

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        try:
            correo= User.objects.get(email=correo)
        except User.DoesNotExist:
            return correo
        raise forms.ValidationError('Correo Electrónico ya registrado')

    def clean_password_2(self):
        password_1=self.cleaned_data['password_1']
        password_2=self.cleaned_data['password_2']

        if password_1==password_2:
            pass
        else:
            raise forms.ValidationError('Las passwords no coinciden')
        