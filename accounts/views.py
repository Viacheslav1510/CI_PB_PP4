# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .forms import RegistrationForm, LoginForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def register(request):
    """
    A function to render sign up page,
    provide registration form
    to register the user in database
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/sign_up.html', context)


class CustomLoginView(LoginView):
    """
    A class to let user log in
    """
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)


def logged_out(request):
    """
    A function to render confirmation log out page,
    provides a form which logs out the user on
    'logout' input
    """
    form = request.POST
    if request.method == 'POST':
        if form.get('logout'):
            logout(request)
            messages.success(request, "You've been logged out")
            return redirect('home')

    return render(request, 'accounts/logout.html')


def logout_confirm(request):
    """
    A function to open log out confirmation
    """
    return render(request, 'accounts/logout.html')
