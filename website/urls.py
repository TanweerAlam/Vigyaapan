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
from django.contrib import admin
from django.urls import path, include
# views for error handler
from . import views
# sitemap
from django.contrib.sitemaps.views import sitemap
from jobs.sitemaps import JobSitemap
sitemaps = {
    'jobs': JobSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include('users.urls', namespace="users.urls")), # users url is imported as accounts path
    # path('users/', include('users.urls', namespace="users")),
    path('', include('main.urls', namespace="main")),
    path('', include('jobs.urls', namespace="jobs")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = "views.page_not_found_view"
# handler500 = "views.server_error_view"
handler403 = "views.permission_denied_view"
# handler400 = "views.bad_request_view"