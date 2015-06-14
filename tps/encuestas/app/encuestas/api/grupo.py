from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.helpers.related_resource_uri_mixin import add_related_uri_to_resource
from encuestas.models.grupo import Grupo
from encuestas.api.pregunta import PreguntaResource



class GrupoResource(ModelResource):
    encuesta = fields.ToOneField('encuestas.api.encuesta.EncuestaResource', 'encuesta')
    preguntas = fields.ToManyField(PreguntaResource, 'preguntas', related_name='grupo', null=True)

    class Meta:
        always_return_data = True
        queryset = Grupo.objects.all()
        resource_name = 'grupo'
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = PrettySerializer()

add_related_uri_to_resource(GrupoResource, 'preguntas', PreguntaResource, 'grupo')
