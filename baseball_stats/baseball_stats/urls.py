from django.conf.urls import patterns, include, url

from django.contrib import admin
import baseball
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', baseball.home),
    url(r'^stats/', include('baseball.urls')),
                       )
