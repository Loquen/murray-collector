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
  path('bills/<int:bill_id>/skill_assoc/<int:skill_id>/', views.skill_assoc, name='skill_assoc'),
  path('bills/<int:bill_id>/remove_skill_assoc/<int:skill_id>/', views.remove_skill_assoc, name='remove_skill_assoc'),
  path('bills/<int:bill_id>/add_photo/', views.add_photo, name='add_photo'),
  path('skills/', views.SkillList.as_view(), name='skills_index'),
  path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skills_detail'),
  path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
  path('skills/<int:pk>/update', views.SkillUpdate.as_view(), name='skills_update'),
  path('skills/<int:pk>/delete', views.SkillDelete.as_view(), name='skills_delete'),

]