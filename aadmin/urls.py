"""aadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#docs
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

APITITLE='pongo'

#schema_view = get_schema_view(title=APITITLE) 

urlpatterns = [

        path('admin/', admin.site.urls),
        path('rest_framework/',include('rest_framework.urls')),
        path('rest_auth/',include('rest_auth.urls')),
        path('account/',include('allauth.urls')),

        ##docs
        path('docs/',include_docs_urls(title=APITITLE)),
 #       path('schema/', schema_view),
        #APP
        #path('api/',include('api.urls')),
        #path('logic/',include('logic.urls')),
]
