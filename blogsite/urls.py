"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import myblog.views
from django.contrib.sitemaps.views import sitemap
from myblog.sitemaps import PostSitemap

sitemaps={
    'posts':PostSitemap,
}
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',myblog.views.post_list,name='post_list'),
    url(r'^myblog/',include('myblog.urls',namespace='myblog',app_name='myblog')),
    url(r'^sitemap\.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]
