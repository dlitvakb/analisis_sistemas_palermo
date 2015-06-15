from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.models.opcion import Opcion


class OpcionResource(ModelResource):
    pregunta = fields.ToOneField('encuestas.api.pregunta.PreguntaResource', 'pregunta')

    class Meta:
        always_return_data = True
        queryset = Opcion.objects.all()
        resource_name = 'opcion'
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = PrettySerializer()

