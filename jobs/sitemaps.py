from django.contrib.sitemaps import Sitemap
from .models import Job, State

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def item(self):
        return Job.objects.filter(isPublished=True)  

    def lastmod(self, obj):
        return obj.created_on