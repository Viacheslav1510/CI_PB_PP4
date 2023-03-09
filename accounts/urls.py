from django.urls import path
from . import views
from accounts.views import CustomLoginView
from accounts.forms import LoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('sign_up/', views.register, name='accounts-register'),
    path(
        'login/',
        CustomLoginView.as_view(
            redirect_authenticated_user=True, 
            template_name='accounts/login.html',
            authentication_form=LoginForm),
        name='accounts-login'
    ),
    path('confirmation/', views.logout_confirm, name='logout-confirmation'),
    path('logout/', views.logged_out, name='logged-out')
]
