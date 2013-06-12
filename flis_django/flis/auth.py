from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from django.conf import settings
from functools import wraps


EDITOR_ROLES = ['Administrator']

COUNTRY_ADMINS = {
    'al': ['eionet-nrc-forwardlooking-cc-al', 'extranet-testrole'],
    'ba': ['eionet-nrc-forwardlooking-cc-ba'],
    'hr': ['eionet-nrc-forwardlooking-cc-hr'],
    'mc': ['eionet-nrc-forwardlooking-cc-mc'],
    'me': ['eionet-nrc-forwardlooking-cc-me'],
    'mk': ['eionet-nrc-forwardlooking-cc-mk'],
    'rs': ['eionet-nrc-forwardlooking-cc-rs'],
    'xk': ['eionet-nrc-forwardlooking-cc-xk'],
    'at': ['eionet-nrc-forwardlooking-mc-at'],
    'be': ['eionet-nrc-forwardlooking-mc-be'],
    'bg': ['eionet-nrc-forwardlooking-mc-bg'],
    'ch': ['eionet-nrc-forwardlooking-mc-ch'],
    'cy': ['eionet-nrc-forwardlooking-mc-cy'],
    'cz': ['eionet-nrc-forwardlooking-mc-cz'],
    'de': ['eionet-nrc-forwardlooking-mc-de'],
    'dk': ['eionet-nrc-forwardlooking-mc-dk'],
    'ee': ['eionet-nrc-forwardlooking-mc-ee'],
    'eea':[ 'eionet-nrc-forwardlooking-mc-eea'],
    'article-5-contribution':[ 'eionet-nrc-forwardlooking-mc-eea'],
    'es': ['eionet-nrc-forwardlooking-mc-es'],
    'fi': ['eionet-nrc-forwardlooking-mc-fi'],
    'fr': ['eionet-nrc-forwardlooking-mc-fr'],
    'gb': ['eionet-nrc-forwardlooking-mc-gb'],
    'gr': ['eionet-nrc-forwardlooking-mc-gr'],
    'hu': ['eionet-nrc-forwardlooking-mc-hu'],
    'ie': ['eionet-nrc-forwardlooking-mc-ie'],
    'is': ['eionet-nrc-forwardlooking-mc-is'],
    'it': ['eionet-nrc-forwardlooking-mc-it'],
    'li': ['eionet-nrc-forwardlooking-mc-li'],
    'lt': ['eionet-nrc-forwardlooking-mc-lt'],
    'lu': ['eionet-nrc-forwardlooking-mc-lu'],
    'lv': ['eionet-nrc-forwardlooking-mc-lv'],
    'mt': ['eionet-nrc-forwardlooking-mc-mt'],
    'nl': ['eionet-nrc-forwardlooking-mc-nl'],
    'no': ['eionet-nrc-forwardlooking-mc-no'],
    'pl': ['eionet-nrc-forwardlooking-mc-pl'],
    'pt': ['eionet-nrc-forwardlooking-mc-pt'],
    'ro': ['eionet-nrc-forwardlooking-mc-ro'],
    'se': ['eionet-nrc-forwardlooking-mc-se'],
    'si': ['eionet-nrc-forwardlooking-mc-si'],
    'sk': ['eionet-nrc-forwardlooking-mc-sk'],
    'tr': ['eionet-nrc-forwardlooking-mc-tr'],
}

def edit_is_allowed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]

        if not getattr(settings, 'SKIP_EDIT_AUTHORIZATION', False):
            roles = getattr(request, 'user_roles', [])
            for role in roles:
                if role in EDITOR_ROLES:
                    return func(*args, **kwargs)
            groups = getattr(request, 'user_groups', [])
            country = request.country.iso
            for group in groups:
                if group[0] in COUNTRY_ADMINS[country]:
                    return func(*args, **kwargs)
            return render(request, 'restricted.html')
        return func(*args, **kwargs)
    return wrapper
