from django.conf.urls import include, url
from django.contrib import admin
from encuestas.api.api import v1_api
from encuestas.views.encuesta import listar_encuestas, exportar_encuesta, \
                                     responder_encuesta, editar_encuesta, \
                                     eliminar_encuesta, nueva_encuesta, \
                                     vista_previa_encuesta, enviar_encuesta, \
                                     gracias
from encuestas.views.home import home


urlpatterns = [
    # Examples:
    # url(r'^$', 'tp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^responder/$', responder_encuesta),
    url(r'^exportar/([0-9]+)/$', exportar_encuesta),
    url(r'^vista_previa/([0-9]+)/$', vista_previa_encuesta),
    url(r'^enviar/([0-9]+)/$', enviar_encuesta),
    url(r'^encuesta/([0-9]+)/$', editar_encuesta),
    url(r'^encuesta/([0-9]+)/delete/$', eliminar_encuesta),
    url(r'^encuestas/new/$', nueva_encuesta),
    url(r'^encuestas/$', listar_encuestas),
    url(r'^gracias/([0-9]+)/$', gracias),
    url(r'^$', home),
]
