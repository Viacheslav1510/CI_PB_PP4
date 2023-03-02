from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.register, name='accounts-register')
]
