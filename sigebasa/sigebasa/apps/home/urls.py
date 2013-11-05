from django.conf.urls import patterns, include, url

urlpatterns = patterns('sigebasa.apps.home.views',
    url(r'^$','inicio',name='inicio'),

)