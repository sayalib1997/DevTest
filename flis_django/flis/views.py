from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse, reverse_lazy

from flis import models


PER_PAGE = 25


class Sources(ListView):

    model = models.Source
    template_name = 'sources.html'
    paginate_by = PER_PAGE


class Source(DetailView):

    model = models.Source
    template_name = 'source.html'


class SourceCreate(CreateView):

    template_name = 'source_edit.html'
    model = models.Source

    def get_context_data(self, *args, **kwargs):
        context = super(SourceCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('sources')
        return context


class SourceEdit(UpdateView):

    template_name = 'source_edit.html'
    model = models.Source

    def get_context_data(self, *args, **kwargs):
        context = super(SourceEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class SourceDelete(DeleteView):

    model = models.Source
    success_url = reverse_lazy('sources')


class Trends(ListView):

    model = models.Trend
    template_name = 'trends.html'
    paginate_by = PER_PAGE


class Trend(DetailView):

    model = models.Trend
    template_name = 'trend.html'


class TrendCreate(CreateView):

    model = models.Trend
    template_name = 'trend_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TrendCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('trends')
        return context


class TrendEdit(UpdateView):

    model = models.Trend
    template_name = 'trend_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TrendCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class TrendDelete(DeleteView):

    model = models.Trend
    success_url = reverse_lazy('trends')


class ThematicCategories(ListView):

    model = models.ThematicCategory
    template_name = 'thematic_categories.html'


class ThematicCategory(DetailView):

    model = models.ThematicCategory
    template_name = 'thematic_category.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ThematicCategory, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('trends')
        return context


class ThematicCategoryCreate(CreateView):

    model = models.ThematicCategory
    template_name = 'thematic_category_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TrendCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('thematic_categories')
        return context


class ThematicCategoryEdit(UpdateView):

    model = models.ThematicCategory
    template_name = 'thematic_category_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ThematicCategoryEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class ThematicCategoryDelete(DeleteView):

    model = models.ThematicCategory
    success_url = reverse_lazy('thematic_categories')


class GeographicalScales(ListView):

    model = models.GeographicalScale
    template_name = 'geographical_scales.html'


class GeographicalScale(DetailView):

    model = models.GeographicalScale
    template_name = 'geographical_scale.html'


class GeographicalScaleCreate(CreateView):

    model = models.GeographicalScale
    template_name = 'geographical_scale_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalScaleCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('geographical_scales')
        return context

class GeographicalScaleEdit(UpdateView):

    model = models.GeographicalScale
    template_name = 'geographical_scale_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalScaleEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GeographicalScaleDelete(DeleteView):

    model = models.GeographicalScale
    success_url = reverse_lazy('geographical_scales')


class GeographicalCoverages(ListView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages.html'


class GeographicalCoverage(DetailView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverage.html'


class GeographicalCoverageCreate(CreateView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverage_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalCoverageCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('geographical_coverages')
        return context


class GeographicalCoverageEdit(UpdateView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverage_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalCoverageEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GeographicalCoverageDelete(DeleteView):

    model = models.GeographicalCoverage
    success_url = reverse_lazy('geographical_coverages')



class SteepCategories(ListView):

    model = models.SteepCategory
    template_name = 'steep_categories.html'


class SteepCategory(DetailView):

    model = models.SteepCategory
    template_name = 'steep_category.html'


class SteepCategoryCreate(CreateView):

    model = models.SteepCategory
    template_name = 'steep_category_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SteepCategoryCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('steep_categories')
        return context


class SteepCategoryEdit(UpdateView):

    model = models.SteepCategory
    template_name = 'steep_category_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SteepCategoryEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class SteepCategoryDelete(DeleteView):

    model = models.SteepCategory
    success_url = reverse_lazy('steep_categories')


class Timelines(ListView):

    model = models.Timeline
    template_name = 'timelines.html'


class Timeline(DetailView):

    model = models.Timeline
    template_name = 'timeline.html'


class TimelineCreate(CreateView):

    model = models.Timeline
    template_name = 'timeline_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TimelineCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('timelines')
        return context


class TimelineEdit(UpdateView):

    model = models.Timeline
    template_name = 'timeline_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TimelineEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class TimelineDelete(DeleteView):

    model = models.Timeline
    success_url = reverse_lazy('timelines')

