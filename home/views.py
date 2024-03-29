# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def home_page(request):
    """
    A fucntion to open home page
    """
    return render(request, 'home/index.html')


@login_required
def contact_page(request):
    """
    A function to open contact us page
    and provide contact form
    """
    if request.method == 'POST':
        email = request.user.email
        contact_form = ContactForm(request.POST, initial={'email': email})
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.info(request, "Massage has been sent")
        return render(request, 'home/message-received.html')
    else:
        email = request.user.email
        contact_form = ContactForm(initial={'email': email})
    context = {
        'contact_form': contact_form
    }
    return render(request, 'home/contact-us.html', context)
