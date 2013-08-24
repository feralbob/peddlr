from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('peddlr.app_urls', namespace='peddlr')),

    url(r'^admin/', include(admin.site.urls)),

)

#if settings.DEBUG and settings.USING_RUNSERVER:
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT, }),
                            )