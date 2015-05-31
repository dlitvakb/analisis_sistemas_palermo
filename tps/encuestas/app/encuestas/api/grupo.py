from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.helpers.related_resource_uri_mixin import add_related_uri_to_resource
from encuestas.models.grupo import Grupo
from encuestas.api.pregunta import PreguntaResource



class GrupoResource(ModelResource):
    preguntas = fields.ToManyField(PreguntaResource, 'preguntas', related_name='grupo')

    class Meta:
        queryset = Grupo.objects.all()
        resource_name = 'grupo'
        authorization = Authorization()
        serializer = PrettySerializer()

add_related_uri_to_resource(GrupoResource, 'preguntas', PreguntaResource, 'grupo')
