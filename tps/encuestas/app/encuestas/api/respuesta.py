from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.models.respuesta import Respuesta


class RespuestaResource(ModelResource):
    class Meta:
        queryset = Respuesta.objects.all()
        resource_name = 'respuesta'
        authorization = Authorization()
        serializer = PrettySerializer()
