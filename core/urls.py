from django.urls import path
from core.views import index_page,kvadrat


urlpatterns = [
    path('',index_page),
    path('kvadrat',kvadrat)
]