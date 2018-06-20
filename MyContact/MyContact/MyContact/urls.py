"""MyContact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from MyContacct import views as contact
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^signup/$', contact.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^contact/$', contact.home, name='home'),
    url(r'^logout/$', contact.logout, name='logout'),
    url(r'^add/$', contact.add, name='add'),
    url(r'^showLogout/$', contact.showLogout, name='showLogout'),
    url(r'^list/$', contact.list, name='list'),
    url(r'^modify/$', contact.modify, name='modify'),
    url(r'^delete/$', contact.delete, name='delete'),
    url(r'^search/$', contact.search, name='search'),
    url(r'^admin/', admin.site.urls),
]