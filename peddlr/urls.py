from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'buy/^$', 'peddlr.views.buy', name='buy'),
    url(r'sell/^$', 'peddlr.views.sell', name='sell'),

    url(r'^$', 'peddlr.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),

)

#if settings.DEBUG and settings.USING_RUNSERVER:
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT, }),
                            )