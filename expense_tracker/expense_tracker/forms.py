from django import forms

class ExpenseForm(forms.Form):
    source_name = forms.CharField(label='Source Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    total_amount = forms.DecimalField(label='Total Amount', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

class ItemForm(forms.Form):
    item_name = forms.CharField(label='Item Name', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))