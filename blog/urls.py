from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='blog-home'),
    path('browse',views.browse, name='browse'),
    path('add',views.add, name='add'),
]