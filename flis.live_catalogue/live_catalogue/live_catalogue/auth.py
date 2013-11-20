from functools import wraps
from django.shortcuts import render


def login_required(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user_id and 'Anonymous' not in request.user_roles:
            return f(request, *args, **kwargs)
        else:
           return render(request, 'restricted.html')
    return wrapper
