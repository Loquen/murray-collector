from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bill, Skill, Photo
import uuid
import boto3
from .forms import BillForm, QuoteForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'collectorofcats'

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
  skills_bill_doesnt_have = Skill.objects.exclude(id__in = bill.skills.all().values_list('id'))
  quote_form = QuoteForm()
  return render(request, 'bills/detail.html', { 
    'bill': bill, 'quote_form': quote_form,
    'skills': skills_bill_doesnt_have
  })

def add_quote(request, bill_id):
  form = QuoteForm(request.POST)
  if form.is_valid():
    new_quote = form.save(commit=False)
    new_quote.bill_id = bill_id
    new_quote.save()
  return redirect('detail', bill_id=bill_id)

def skill_assoc(request, bill_id, skill_id):
  Bill.objects.get(id=bill_id).skills.add(skill_id)
  return redirect('detail', bill_id=bill_id)

def remove_skill_assoc(request, bill_id, skill_id):
  Bill.objects.get(id=bill_id).skills.remove(skill_id)
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

class SkillList(ListView):
  model = Skill

class SkillDetail(DetailView):
  model = Skill

class SkillCreate(CreateView):
  model = Skill
  fields = '__all__'

class SkillUpdate(UpdateView):
  model = Skill
  fields = ['level']

class SkillDelete(DeleteView):
  model = Skill
  success_url = '/skills/'

def add_photo(request, bill_id):
    # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    print(key)
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      print(url)
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, bill_id=bill_id)
      print(photo)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', bill_id=bill_id)
