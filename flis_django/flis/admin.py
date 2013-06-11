from django.contrib import admin
from django.contrib.auth.models import  Group
from flis import models


class CountryAdmin(admin.ModelAdmin):
    model = models.Country
    search_fields = ['iso', 'name']
    list_display = ('iso', 'name')


admin.site.register(models.Country, CountryAdmin)
admin.site.unregister(Group)