from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from django.conf import settings
from functools import wraps


EDITOR_ROLES = ['Authenticated']


def edit_is_allowed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]

        if not getattr(settings, 'SKIP_EDIT_AUTHORIZATION', False):
            roles = getattr(request, 'user_roles', [])
            for role in roles:
                if role in EDITOR_ROLES:
                    return func(*args, **kwargs)
            return render(request, 'restricted.html')
        return func(*args, **kwargs)
    return wrapper
