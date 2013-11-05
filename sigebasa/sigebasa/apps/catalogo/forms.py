from django import forms
from sigebasa.apps.catalogo.models import Hospital,Producto,Pedido

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido




