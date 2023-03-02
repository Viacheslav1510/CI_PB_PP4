from django.shortcuts import render, redirect
from .forms import RegistrationForm


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
