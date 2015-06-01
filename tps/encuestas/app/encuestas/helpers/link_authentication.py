from tastypie.authentication import Authentication

class LinkAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if request.session.get('link_hash', False):
            return True
        return False

    def get_identifier(self, request):
        return request.session.get('link_hash', False)
