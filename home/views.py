from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm


def home_page(request):
    return render(request, 'home/index.html')


@login_required
def contact_page(request):
    # user_email = request.user.email
    # user = User.objects.filter(email=user_email).first()
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