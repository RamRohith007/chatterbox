from django.contrib import admin
from django.contrib.admin import register
from .models import Box, Messages

# Register your models here.
admin.site.register(Box)
admin.site.register(Messages)