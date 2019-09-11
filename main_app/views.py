from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Bill
from .forms import BillForm, QuoteForm

# Create your views here.
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def bills_index(request):
  bills = Bill.objects.all()
  return render(request, 'bills/index.html', { 'bills': bills })

def bills_detail(request, bill_id):
  bill = Bill.objects.get(id=bill_id)
  quote_form = QuoteForm()
  return render(request, 'bills/detail.html', { 
    'bill': bill, 'quote_form': quote_form })

def add_quote(request, bill_id):
  form = QuoteForm(request.POST)
  if form.is_valid():
    new_quote = form.save(commit=False)
    new_quote.bill_id = bill_id
    new_quote.save()
  return redirect('detail', bill_id=bill_id)

def bill_new(request):
  if request.method == "POST":
    form = BillForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = BillForm()
    return render(request, 'bills/bill_edit.html', {'form': form})

class BillUpdate(UpdateView):
  model = Bill
  fields = '__all__'

class BillDelete(DeleteView):
  model = Bill
  success_url = '/bills/'