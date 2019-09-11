from django.contrib import admin
from .models import Bill, Quote, Skill, Photo
# Register your models here.

admin.site.register(Bill)
admin.site.register(Quote)
admin.site.register(Skill)
admin.site.register(Photo)