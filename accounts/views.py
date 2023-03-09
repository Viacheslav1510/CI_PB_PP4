from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages


def register(request):
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
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


def logout_confirm(request):
    form = request.POST
    if request.method == 'POST':
        if form.get('logout'):
            logout(request)
            messages.success(request, "You've been logged out")
            return redirect('home')
        else:
            return render(request, 'home/index.html')

    return render(request, 'accounts/logout.html')


def logged_out(request):
    return render(request, 'accounts/logout.html')
