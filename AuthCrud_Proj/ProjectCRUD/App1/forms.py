from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields='__all__'

    def clean_quantity(self):
        q=self.cleaned_data['quantity']
        if q<1:
            raise forms.ValidationError('Quantity must be greater than zero!')
        return q