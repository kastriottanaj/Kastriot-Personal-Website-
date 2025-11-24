from django.urls import path
from .feeds import LatestPostsFeed
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog"),
    path("kategorie/<slug:category_slug>/", views.blog_list, name="blog_by_category"),  
    path("rss/", LatestPostsFeed(), name="blog_rss"),
    path("<slug:slug>/", views.blog_detail, name="blog_detail"),
]
