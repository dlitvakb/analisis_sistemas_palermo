from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.helpers.related_resource_uri_mixin import add_related_uri_to_resource
from encuestas.models.encuesta import Encuesta
from encuestas.api.grupo import GrupoResource


class EncuestaResource(ModelResource):
    grupos = fields.ToManyField(GrupoResource, 'grupos', related_name='encuesta')
    creador = fields.ForeignKey('encuestas.api.user.UserResource', 'creador')

    class Meta:
        queryset = Encuesta.objects.all()
        resource_name = 'encuesta'
        authorization = Authorization()
        serializer = PrettySerializer()

add_related_uri_to_resource(EncuestaResource, 'grupos', GrupoResource, 'encuesta')
