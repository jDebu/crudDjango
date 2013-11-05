from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'sigebasa.apps.catalogo.views.ver', name='ver'),
    #url(r'^$','sigebasa.apps.catalogo.views.metroboot', name='metroboot'),
    #url(r'^base/','sigebasa.apps.catalogo.views.metrobootbase', name='metrobootbase'),
    #url(r'^components/','sigebasa.apps.catalogo.views.metrobootcomponents', name='metrobootcomponents'),
    # url(r'^sigebasa/', include('sigebasa.foo.urls')),
    url(r'^hospitales/',include('sigebasa.apps.catalogo.urls',namespace='catalogo')),
    url(r'^home/',include('sigebasa.apps.home.urls',namespace='home')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
