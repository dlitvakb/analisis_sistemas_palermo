from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.helpers.link_authentication import LinkAuthentication
from encuestas.models.respuesta import Respuesta


class RespuestaResource(ModelResource):
    opcion = fields.ToOneField('encuestas.api.opcion.OpcionResource', 'opcion')
    encuesta = fields.ToOneField('encuestas.api.encuesta.EncuestaResource', 'encuesta')
    usuario = fields.ToOneField('encuestas.api.user.UserResource', 'usuario')

    class Meta:
        always_return_data = True
        queryset = Respuesta.objects.all()
        resource_name = 'respuesta'
        authorization = Authorization()
        authentication = LinkAuthentication()
        serializer = PrettySerializer()
