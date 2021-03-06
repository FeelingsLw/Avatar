"""Avatar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

import Speech.urls
import Face.urls
import Jokes.urls

router_v1 = routers.DefaultRouter()
Jokes.urls.regRouter(router_v1)

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),

    url(r'^speech/', include(Speech.urls)),
    url(r'^face/', include(Face.urls)),

    #Restful Api
    url(r'^api/v1/', include(router_v1.urls)),
    url(r'^api/v2/', include(Jokes.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
