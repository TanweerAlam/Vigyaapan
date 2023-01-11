from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['main:about', 'main:contact', 'main:privacy-policy', 'main:disclaimer', 'main:tnc', 'jobs:jobList', 'jobs:search_results', 'jobs:tagList',]

    def location(self, item):
        return reverse(item)
        # return f'/{item}'