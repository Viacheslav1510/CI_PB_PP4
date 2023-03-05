from django.shortcuts import render, redirect
from .forms import RegistrationForm
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
