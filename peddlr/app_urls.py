from django.conf.urls import patterns, url


urlpatterns = patterns('peddlr.views',
    url(r'^$', 'home', name='home'),
    url(r'buy/$', 'buy', name='buy'),
    url(r'sell/$', 'sell', name='sell'),
)
