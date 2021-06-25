# apps/accounts/urls.py

from django.urls import path
from apps.accounts import views 

urlpatterns = [
    path('registrasi/', 
    	views.registrasiView,
    	name='registrasi_view'),
]