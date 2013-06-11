import re
from path import path
from django import template
from django.db.models import Q
from django.conf import settings
from flis.models import Interlink


register = template.Library()


@register.simple_tag
def active(request, pattern):
    pattern = '^%s/%s/' + pattern
    if getattr(settings, 'FORCE_SCRIPT_NAME', None):
        pattern = pattern % (settings.FORCE_SCRIPT_NAME, request.country)
    else:
        pattern = pattern % ('', request.country)

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


@register.filter
def get_interlinks(indicator):
    interlinks = Interlink.objects.filter(
        Q(indicator_1=indicator) | Q(indicator_2=indicator) |
        Q(indicator_3=indicator) | Q(indicator_4=indicator)).distinct()

    return interlinks


@register.filter
def get_gmts_from_interlinks(interlinks):
    gmts = set()
    for interlink in interlinks:
        gmts.add(interlink.gmt)
    return gmts


@register.filter
def get_trends_from_interlinks(interlinks):
    trends = set()
    for interlink in interlinks:
        trends.add(interlink.trend)
    return trends
