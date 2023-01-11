from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['main:about', 'main:contact', 'main:privacy-policy', 'main:disclaimer', 'main:tnc', 'jobs:jobList', 'jobs:list_by_type', 'jobs:search_results', 'jobs:tagList', 'jobs:job_list_by_tags', 'jobs:jobDetail']

    def location(self, item):
        return reverse(item)
        # return f'/{item}'