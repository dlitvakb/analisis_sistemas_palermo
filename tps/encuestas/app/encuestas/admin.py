import json
from django.http import HttpResponse
from django.contrib import admin

from .models import encuesta
from .models import grupo
from .models import link
from .models import opcion
from .models import pregunta
from .models import user
from .models import respuesta



class OpcionInline(admin.TabularInline):
    model = opcion.Opcion
    extra = 3


class PreguntaInline(admin.TabularInline):
    model = pregunta.Pregunta
    extra = 5


class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]


class GrupoInline(admin.TabularInline):
    model = grupo.Grupo
    extra = 2


class GrupoAdmin(admin.ModelAdmin):
    inlines = [PreguntaInline]


class EncuestaAdmin(admin.ModelAdmin):
    inlines = [GrupoInline]
    actions = ['generar_links', 'exportar_encuesta']

    def generar_links(self, request, encuestas):
        for encuesta in encuestas.all():
            encuesta.generar_links()

    def exportar_encuesta(self, request, encuestas):
        export = {}

        for encuesta in encuestas.all():
            try:
                export["%d - %s" % (encuesta.id, encuesta.nombre)] = \
                        encuesta.exportar()
            except Exception, e:
                import ipdb; ipdb.set_trace()
                continue

        export["cantidad_encuestas"] = encuestas.count()
        export["cantidad_encuestas_finalizadas"] = len([ e for e in encuestas.all() if e._is_finalized() ])

        response = HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="%s.json"' % ("Export Encuestas",)
        response.write(json.dumps(export, sort_keys=True, indent=2, separators=(',', ': ')))

        return response




# Register your models here.
admin.site.register(encuesta.Encuesta, EncuestaAdmin)
admin.site.register(grupo.Grupo, GrupoAdmin)
admin.site.register(pregunta.Pregunta, PreguntaAdmin)

admin.site.register(link.Link)

admin.site.register(user.User)

admin.site.register(respuesta.Respuesta)
