from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.helpers.related_resource_uri_mixin import add_related_uri_to_resource
from encuestas.models.encuesta import Encuesta
from encuestas.api.grupo import GrupoResource
from encuestas.api.user import UserResource


class EncuestaResource(ModelResource):
    grupos = fields.ToManyField(GrupoResource, 'grupos', related_name='encuesta', null=True)
    usuarios = fields.ToManyField(UserResource, 'usuarios', related_name='encuestas', null=True)

    class Meta:
        always_return_data = True
        queryset = Encuesta.objects.all()
        resource_name = 'encuesta'
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = PrettySerializer()

add_related_uri_to_resource(EncuestaResource, 'grupos', GrupoResource, 'encuesta')
