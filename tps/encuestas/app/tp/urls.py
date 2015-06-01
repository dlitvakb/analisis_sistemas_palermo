from django.conf.urls import include, url
from django.contrib import admin
from encuestas.api.api import v1_api
from encuestas.views.responder_encuesta import responder_encuesta


urlpatterns = [
    # Examples:
    # url(r'^$', 'tp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^responder/', responder_encuesta),
]
