from django.conf.urls import url
from django.core.urlresolvers import reverse
from tastypie.utils import trailing_slash


class RelatedResourceURIMixin(object):
    def __init__(self, related_resource_class, related_resource_name, related_resource_fk_field_name):
        self._related_resource_class = related_resource_class
        self._related_resource_name = related_resource_name
        self._related_resource_url_name = 'api_get_{}_for_{}'.format(self._related_resource_name,
                                                                     self._meta.resource_name)

    def _related_resource_view(self, request, **kwargs):
        self.method_check(request, ['get', ])
        return related_resource_class().get_list(request, **{related_resource_fk_field_name: kwargs['pk']})

    def dehydrate(self, bundle):
        kwargs = dict(api_name='v1', resource_name=self._meta.resource_name, pk=bundle.data['id'])
        bundle.data['{}_uri'.format(self._related_resource_name)] = \
            reverse(self._related_resource_url_name, kwargs=kwargs)

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>{})/(?P<pk>\w[\w/-]*)/{}{}$'.format(self._meta.resource_name,
                                                                         self._related_resource_name,
                                                                         trailing_slash()),
                self.wrap_view('_related_resource_view'),
                name=self._related_resource_url_name)
        ]

def patch_class_func(cls, func_name):
    def wrapped_new_func(new_func):
        orig_func = getattr(cls, func_name)
        def call_new_func_on_return_value_of_old(self, *args, **kwargs):
            return new_func(self, orig_func(self, *args, **kwargs))
        setattr(cls, func_name, call_new_func_on_return_value_of_old)
    return wrapped_new_func

def add_related_uri_to_resource(resource_class, related_resource_name, related_resource_class, related_resource_fk_field_name):
    base_resource_name = resource_class.Meta.resource_name

    uri_key = '{}_uri'.format(related_resource_name)
    url_name = 'api_get_{}_for_{}'.format(related_resource_name, base_resource_name)
    view_func_name = 'get_{}'.format(related_resource_name)

    @patch_class_func(resource_class, 'dehydrate')
    def wrap_dehydrate(self, dehydrated_bundle):
        # build related resource URI
        kwargs = dict(api_name='v1', resource_name=base_resource_name, \
                      pk=dehydrated_bundle.data[self._meta.object_class._meta.pk.name])
        dehydrated_bundle.data[uri_key] = reverse(url_name, kwargs=kwargs)
        return dehydrated_bundle

    @patch_class_func(resource_class, 'prepend_urls')
    def wrap_prepend_urls(self, url_list):
        # copy the detail URL for the base resource
        dispatch_detail_url = [u for u in self.base_urls() if u.name == 'api_dispatch_detail'][0]

        # append the related resource name to it
        related_url_pattern = dispatch_detail_url.regex.pattern.rstrip('$?/')
        related_url_pattern = r'{}/{}{}$'.format(related_url_pattern, related_resource_name, trailing_slash())

        # and create the URL pattern for the related resource list view
        url_list.append(url(related_url_pattern, self.wrap_view(view_func_name), name=url_name))
        return url_list

    def get_related_list(self, request, **kwargs):
        # allow only GET requests on the related resource list
        self.method_check(request, str('get'))
        return related_resource_class().get_list(request, **{related_resource_fk_field_name: kwargs['pk']})

    setattr(resource_class, view_func_name, get_related_list)
