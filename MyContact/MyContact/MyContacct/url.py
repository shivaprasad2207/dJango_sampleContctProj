from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('', views.signup, name='signup'),
    path('', views.logout, name='logout'),
    path('', views.showLogout, name='showLogout'),
    path('', views.logout, name='logout'),
    path('', views.add, name='add'),
    path('', views.list, name='list'),
    path('', views.modify, name='modify'),
    path('', views.delete, name='delete'),
    path('', views.search, name='search'),

]