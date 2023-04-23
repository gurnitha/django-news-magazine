# app/main/admin.py

from django.contrib import admin

# Import from locals
from app.main.models import Main

# Register your models here.

admin.site.register(Main)