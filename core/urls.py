# Create url here
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ueber-uns/', views.about, name='about'),  # Über Uns
    path('datenschutz/', views.privacy, name='privacy'),  # Datenschutz
    path('privacy/', views.datenschutz, name='datenschutz'), # Impressum
    path('services/', views.services, name='services'),  # Unsere Dienstleistungen
    path('branchen/', views.branchen, name='branchen'),  # Branchen
    path('industries/', lambda request: redirect('branchen', permanent=True)),  # 👈 Redirects /industries/ to /branchen/
    #path('blog/', views.blog, name='blog'),  # Blog
    path('testimonials/', views.testimonials, name='testimonials'),  # Kundenmeinungen
    path('kontakt/', views.kontakt, name='kontakt'), # Kontakt
    path('contact/', lambda request: redirect('kontakt', permanent=True)), # ✅ Redirect from /contact/ to /kontakt/ for safety and UX
    path("impressum/", views.impressum, name="impressum"),
    path("robots.txt", views.robots_txt, name="robots"),
]