from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        # return ['jobs/search', 'jobs/list_by_result', 'jobs/list_by_admit-card', 'jobs/list_by_answerkey', 'about', 'contact', 'privacy-policy', 'disclaimer', 'tnc', 'contact', ]
        return ['main:about', 'main:contact', 'main:privacy-policy', 'main:disclaimer', 'main:tnc']

    def location(self, item):
        return reverse(item)
        # return f'/{item}'