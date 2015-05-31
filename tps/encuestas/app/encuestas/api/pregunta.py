from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.helpers.related_resource_uri_mixin import add_related_uri_to_resource
from encuestas.models.pregunta import Pregunta
from encuestas.api.opcion import OpcionResource


class PreguntaResource(ModelResource):
    opciones = fields.ToManyField(OpcionResource, 'opciones', related_name='pregunta', full=True)

    class Meta:
        queryset = Pregunta.objects.all()
        resource_name = 'pregunta'
        authorization = Authorization()
        serializer = PrettySerializer()

add_related_uri_to_resource(PreguntaResource, 'opciones', OpcionResource, 'pregunta')