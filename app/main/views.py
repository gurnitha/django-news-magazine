# app/main/views.py

# Import django/third parties modules
from django.shortcuts import render, get_object_or_404, redirect

# Import from locals
from app.main.models import Main

# Create your views here.

def home_page(request):

	return render(request, 'main/home_page.html');
