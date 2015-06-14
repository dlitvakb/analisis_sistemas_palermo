from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.helpers.link_authentication import LinkAuthentication
from encuestas.models.respuesta import Respuesta


class RespuestaResource(ModelResource):
    class Meta:
        always_return_data = True
        queryset = Respuesta.objects.all()
        resource_name = 'respuesta'
        authorization = Authorization()
        authentication = LinkAuthentication()
        serializer = PrettySerializer()
