from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', views.register, name='accounts-register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='accounts-login'
    ),
    path('confirmation/', views.logout_confirm, name='logout-confirmation'),
    path('logout/', views.logged_out, name='logged-out')
]
