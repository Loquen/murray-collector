from django import forms

from .models import Bill, Quote

class BillForm(forms.ModelForm):
  class Meta:
    model = Bill
    fields = ('name', 'movie', 'description', 'release',)

class QuoteForm(forms.ModelForm):
  class Meta:
    model = Quote
    fields = ('text',)
