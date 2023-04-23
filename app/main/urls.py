# app/main/urls.py

# Import django/third parties modules
from django.urls import path
from django.conf.urls import url

# Import from locals
from app.main import views

app_name = 'main'

urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
]