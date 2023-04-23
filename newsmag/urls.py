from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [

    url(r'^admin/' , admin.site.urls),

    # url untuk main app
    url(r'', include('app.main.urls')),
    
]
