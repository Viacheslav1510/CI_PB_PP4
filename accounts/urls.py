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
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
        name='accounts-logout'
    ),
]
