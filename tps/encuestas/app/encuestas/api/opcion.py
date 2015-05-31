from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.models.opcion import Opcion


class OpcionResource(ModelResource):
    class Meta:
        queryset = Opcion.objects.all()
        resource_name = 'opcion'
        authorization = Authorization()
        serializer = PrettySerializer()

