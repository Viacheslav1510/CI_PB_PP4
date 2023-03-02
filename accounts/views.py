from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/sign_up.html', context)
