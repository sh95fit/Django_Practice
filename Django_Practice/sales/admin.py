from django.contrib import admin
from .models import CustomID, Sale, Person
# Register your models here.
admin.site.register(CustomID)
admin.site.register(Sale)
admin.site.register(Person)
