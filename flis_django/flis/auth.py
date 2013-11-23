from functools import wraps
from itertools import chain

from django.shortcuts import render
from django.conf import settings

from constants import EDITOR_ROLES, COUNTRY_ADMINS


def _check_perm(roles, groups, country):
    for role in roles:
        if role in EDITOR_ROLES:
            return True

    for group in groups:
        if country:
            if group[0] in COUNTRY_ADMINS[country]:
                return True
        else:
            # flatten COUNTRY_ADMINS.values()
            if group[0] in list(chain(*COUNTRY_ADMINS.values())):
                return True
    return False


def edit_is_allowed(f, check_country=False):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if not getattr(settings, 'SKIP_EDIT_AUTHORIZATION', False):
            roles = getattr(request, 'user_roles', [])
            groups = getattr(request, 'user_groups', [])
            country = request.country.iso if check_country else None
            if not _check_perm(roles, groups, country):
                return render(request, 'restricted.html')
        return f(request, *args, **kwargs)
    return wrapper
