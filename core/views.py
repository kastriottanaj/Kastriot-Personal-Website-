# core/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from datetime import datetime
from .forms import ContactForm
from .models import ContactMessage 

def home(request):
    return render(request, 'home.html', {'now': datetime.now().year})

def about(request):
    return render(request, 'about.html', {'title': 'Über Uns'})

def datenschutz(request):
    return render(request, 'datenschutz.html', {'title': 'Datenschutz'})

def privacy(request):
    return render(request, 'datenschutz.html', {'title': 'Datenschutzerklärung'})

def services(request):
    return render(request, 'services.html', {'title': 'Unsere Dienstleistungen'})

def branchen(request):
    return render(request, 'branchen.html', {'title': 'Branchen'})

#def blog(request):
    #return render(request, 'blog.html', {'title': 'Blog'})

def testimonials(request):
    return render(request, 'testimonials.html', {'title': 'Kundenmeinungen'})

def kontakt(request):
    return render(request, 'kontakt.html', {'title': 'Kontakt'})

def impressum(request):
    return render(request, "impressum.html", {"title": "Impressum"})

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: https://yourdomain.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def kontakt(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # Send email
            send_mail(
                subject=f"Neue Kontaktanfrage von {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )

            success = True
            form = ContactForm()  # reset
    else:
        form = ContactForm()

    return render(request, 'kontakt.html', {
        'form': form,
        'success': success,
    })