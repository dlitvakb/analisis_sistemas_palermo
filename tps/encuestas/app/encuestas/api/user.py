from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from encuestas.helpers.pretty_serializer import PrettySerializer
from encuestas.models.user import User


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = PrettySerializer()
        fields = ["mail"]

