from django.shortcuts import get_object_or_404
from django.conf import settings
from flis.models import Country


class CountryMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        management_url = '%s/management' % (settings.FORCE_SCRIPT_NAME)
        code = view_kwargs.pop('country', 'eea')
        if not request.path.startswith(management_url):
            request.country = get_object_or_404(Country, pk=code)
        else:
            request.country = None
