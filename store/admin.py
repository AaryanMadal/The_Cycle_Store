from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Cycles)
admin.site.register(Contact)
admin.site.register(Order)
