from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.models.link import Link


class LinkResource(ModelResource):
    class Meta:
        queryset = Link.objects.all()
        resource_name = 'link'
        authorization = Authorization()
        serializer = PrettySerializer()

