"""
URL configuration for mkplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('show_things/', show_things, name='show_things'),
    path('add_thing/', add_thing, name='add_thing'),
    path('show_things/<int:thing_id>', thing_detail, name='one_thing'),
    path('suplier/add/', SuplierCreateView.as_view(), name='suplier_app'),
    path('show_suplier/', SuplierListView.as_view(), name='show_suplier'),
    path('show_suplier/<int:suplier_id>', SuplierDetailView.as_view(), name='one_show_suplier'),
    path('show_suplier/edit/<int:pk>', SuplierUpdateView.as_view(), name='edit_suplier'),
    path('show_suplier/delete/<int:pk>', SuplierDeleteView.as_view(), name='delete_suplier'),
    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log_in'),
    path('logout/', user_logout, name='log_out'),
    path('email/', contact_email, name='email'),
    path('api/list/', thing_api_list, name='thing_api_list'),
    path('api/detail/<int:pk>', thing_api_detail, name='thing_api_detail'),
]
