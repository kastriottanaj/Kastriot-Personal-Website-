# blog/feeds.py
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import BlogPost

class LatestPostsFeed(Feed):
    title = "PolePosition Automation – Blog Feed"
    link = "/blog/"
    description = "Aktuelle Artikel zur Prozessautomatisierung und Digitalisierung."

    def items(self):
        return BlogPost.objects.filter(published=True).order_by('-created_at')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.meta_description or item.content[:200]

    def item_link(self, item):
        return reverse("blog_detail", args=[item.slug])
