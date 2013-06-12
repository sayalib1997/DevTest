from django.shortcuts import render
from django.conf import settings
from functools import wraps

from constants import EDITOR_ROLES, COUNTRY_ADMINS

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
