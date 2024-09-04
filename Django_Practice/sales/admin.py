from django.contrib import admin
from .models import CustomID, Sale, Person, UserProfile
# Register your models here.
admin.site.register(CustomID)
admin.site.register(Sale)
admin.site.register(UserProfile)
admin.site.register(Person)
