from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('bills/', views.bills_index, name='index'),
  path('bills/<int:bill_id>/', views.bills_detail, name='detail'),
  path('bill/new/', views.bill_new, name='bill_new'),
  path('bills/<int:pk>/update', views.BillUpdate.as_view(), name='bills_update'),
  path('bills/<int:pk>/delete', views.BillDelete.as_view(), name='bills_delete'),
  path('bills/<int:bill_id>/add_quote', views.add_quote, name='add_quote'),
]