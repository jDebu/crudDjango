from django.conf.urls import patterns, include, url

urlpatterns = patterns('sigebasa.apps.catalogo.views',
    url(r'^$','ver',name='ver'),
    url(r'^crear/$','crear', name='crear'),
    url(r'^borrar/(?P<id>\d+)$','borrar',name='borrar'),
    url(r'^actualizar/(?P<id>\d+)$','actualizar',name='actualizar'),
)