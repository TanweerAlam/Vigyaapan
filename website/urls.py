"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from . import views

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# views for error handler
# from . import views
# sitemap
# from django.contrib.sitemaps import views as sitemaps_views
from django.contrib.sitemaps.views import sitemap, index
from .sitemaps import StaticViewSitemap
from jobs.sitemaps import JobSitemap
from django.views.decorators.cache import cache_page


sitemaps = {
    'static': StaticViewSitemap,
    'jobs': JobSitemap,
}

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('not_for_you/secret_gate/panel_control', admin.site.urls),
    # path('accounts/', include("django.contrib.auth.urls")),
    # path('accounts/', include('users.urls', namespace="users.urls")), # users url is imported as accounts path
    # path('tinymce/', include('tinymce.urls')),
    # path('users/', include('users.urls', namespace="users")),
    path('newsletters/', include('newsletters.urls', namespace="newsletters")),
    path('', include('main.urls', namespace="main")),
    path('', include('jobs.urls', namespace="jobs")),
    path('sitemap.xml', cache_page(86400)(index), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.index'),
    path('sitemap-<section>.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('taggit_autosuggest', include('taggit_autosuggest.urls')),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = "views.page_not_found_view"
# # handler500 = "views.server_error_view"
# handler403 = "views.permission_denied_view"
# # handler400 = "views.bad_request_view"