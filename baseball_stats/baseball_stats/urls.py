from django.conf.urls import include, url

from django.contrib import admin
from baseball.views import home
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^stats/', include('baseball.urls')),
]
