from functools import wraps
from django.conf import settings
from django.shortcuts import render


def login_required(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if not getattr(settings, 'SKIP_EDIT_AUTHORIZATION', False):
            if request.user_id and 'Anonymous' not in request.user_roles:
                pass
            else:
               return render(request, 'restricted.html')
        return f(request, *args, **kwargs)
    return wrapper
