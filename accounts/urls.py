# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
from accounts.views import CustomLoginView
from accounts.forms import LoginForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
    path('confirmation/', views.logged_out, name='logout-confirmation'),
    path('logout/', views.logout_confirm, name='logged-out')
]
