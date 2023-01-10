from django.contrib.sitemaps import Sitemap
from .models import Job, State
from django.urls import reverse

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    limit = 3

    def items(self):
        return Job.objects.filter(is_published=True)

    def lastmod(self, obj):
        # return obj.created_on
        return obj.updated_on

class CategorialJobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    limit = 500

    def items(self):
        return ['jobs:jobList', 'jobs:list_by_type', 'jobs:search_results']

    def lastmod(self, obj):
        # return obj.created_on
        return obj.updated_on