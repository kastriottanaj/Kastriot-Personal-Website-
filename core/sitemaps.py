from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'home',
            'about',
            'services',
            'branchen',
            'blog',
            'testimonials',
            'kontakt',
            'impressum',
            'privacy',
        ]

    def location(self, item):
        return reverse(item)
