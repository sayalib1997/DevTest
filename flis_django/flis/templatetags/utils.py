import re
from path import path
from django import template


register = template.Library()


@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return ''


@register.filter
def filename(value):
    return path(value.file.name).basename()


@register.filter
def has_referenced_items(thing):
    items = get_referenced_items(thing)
    return len(items) > 0


@register.filter
def get_referenced_items(thing):
    referenced_items = {}
    for item in thing._meta.get_all_related_objects():
        accesor_name = item.get_accessor_name()
        related_manager = getattr(thing, accesor_name)
        if related_manager.count() > 0:
            referenced_items[accesor_name] = related_manager.all()
    return referenced_items.items()


@register.filter
def remove_underscore(value):
    return value.replace('_', ' ')