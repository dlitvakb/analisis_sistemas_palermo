from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.models.link import Link


class LinkResource(ModelResource):
    class Meta:
        always_return_data = True
        queryset = Link.objects.all()
        resource_name = 'link'
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = PrettySerializer()

