# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url


urlpatterns = [
    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('api', views.api, name='api'),
    path('complain.html', views.forms, name='forms'),
    re_path(r'^delete/', views.delete, name='delete'),
]
