from django.contrib import admin

from .models import encuesta
from .models import grupo
from .models import link
from .models import opcion
from .models import pregunta
from .models import user



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


def generar_links(modeladmin, request, encuestas):
    for encuesta in encuestas.all():
        encuesta.generar_links()

class EncuestaAdmin(admin.ModelAdmin):
    inlines = [GrupoInline]
    actions = [generar_links]


# Register your models here.
admin.site.register(encuesta.Encuesta, EncuestaAdmin)
admin.site.register(grupo.Grupo, GrupoAdmin)
admin.site.register(pregunta.Pregunta, PreguntaAdmin)

admin.site.register(link.Link)

admin.site.register(user.User)
