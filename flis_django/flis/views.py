from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse, reverse_lazy

from flis import models, auth


PER_PAGE = 25


class Interlinks(ListView):

    model = models.Interlink
    template_name = 'interlinks/interlinks.html'
    paginate_by = PER_PAGE

    @method_decorator(auth.is_view_excluded('interlinks'))
    def dispatch(self, *args, **kwargs):
        return super(Interlinks, self).dispatch(*args, **kwargs)


class Interlink(DetailView):

    model = models.Interlink
    template_name = 'interlinks/interlink.html'
    paginate_by = PER_PAGE

    @method_decorator(auth.is_view_excluded('interlinks'))
    def dispatch(self, *args, **kwargs):
        return super(Interlink, self).dispatch(*args, **kwargs)


class InterlinkCreate(CreateView):

    model = models.Interlink
    template_name = 'interlinks/interlink_edit.html'

    @method_decorator(auth.is_view_excluded('interlinks'))
    def dispatch(self, *args, **kwargs):
        return super(InterlinkCreate, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(InterlinkCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('interlinks')
        return context


class InterlinkEdit(UpdateView):
    model = models.Interlink
    template_name = 'interlinks/interlink_edit.html'

    @method_decorator(auth.is_view_excluded('interlinks'))
    def dispatch(self, *args, **kwargs):
        return super(InterlinkEdit, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(InterlinkEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class InterlinkDelete(DeleteView):

    model = models.Interlink
    success_url = reverse_lazy('interlinks')

    @method_decorator(auth.is_view_excluded('interlinks'))
    def dispatch(self, *args, **kwargs):
        return super(InterlinkDelete, self).dispatch(*args, **kwargs)


class Sources(ListView):

    model = models.Source
    template_name = 'sources/sources.html'
    paginate_by = PER_PAGE


    @method_decorator(auth.is_view_excluded('sources'))
    def dispatch(self, *args, **kwargs):
        return super(Sources, self).dispatch(*args, **kwargs)


class Source(DetailView):

    model = models.Source
    template_name = 'sources/source.html'

    @method_decorator(auth.is_view_excluded('sources'))
    def dispatch(self, *args, **kwargs):
        return super(Source, self).dispatch(*args, **kwargs)


class SourceCreate(CreateView):

    template_name = 'sources/source_edit.html'
    model = models.Source

    @method_decorator(auth.is_view_excluded('sources'))
    def dispatch(self, *args, **kwargs):
        return super(SourceCreate, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SourceCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('sources')
        return context


class SourceEdit(UpdateView):

    template_name = 'sources/source_edit.html'
    model = models.Source

    @method_decorator(auth.is_view_excluded('sources'))
    def dispatch(self, *args, **kwargs):
        return super(SourceEdit, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SourceEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class SourceDelete(DeleteView):

    model = models.Source
    success_url = reverse_lazy('sources')

    @method_decorator(auth.is_view_excluded('sources'))
    def dispatch(self, *args, **kwargs):
        return super(SourceDelete, self).dispatch(*args, **kwargs)


class GMTs(ListView):

    model = models.GMT
    template_name = 'gmt/gmts.html'
    paginate_by = PER_PAGE

    @method_decorator(auth.is_view_excluded('gmts'))
    def dispatch(self, *args, **kwargs):
        return super(SourceDelete, self).dispatch(*args, **kwargs)


class GMT(DetailView):

    model = models.GMT
    template_name = 'gmt/gmt.html'

    @method_decorator(auth.is_view_excluded('gmts'))
    def dispatch(self, *args, **kwargs):
        return super(GMT, self).dispatch(*args, **kwargs)


class GMTCreate(CreateView):

    model = models.GMT
    template_name = 'gmt/gmt_edit.html'

    @method_decorator(auth.is_view_excluded('gmts'))
    def dispatch(self, *args, **kwargs):
        return super(GMTCreate, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(GMTCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('gmts')
        return context


class GMTEdit(UpdateView):

    model = models.GMT
    template_name = 'gmt/gmt_edit.html'

    @method_decorator(auth.is_view_excluded('gmts'))
    def dispatch(self, *args, **kwargs):
        return super(GMTEdit, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(GMTEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GMTDelete(DeleteView):

    model = models.GMT
    success_url = reverse_lazy('gmts')

    @method_decorator(auth.is_view_excluded('gmts'))
    def dispatch(self, *args, **kwargs):
        return super(GMTDelete, self).dispatch(*args, **kwargs)


class Indicators(ListView):

    model = models.Indicator
    template_name = 'indicators/indicators.html'

    @method_decorator(auth.is_view_excluded('indicators'))
    def dispatch(self, *args, **kwargs):
        return super(Indicators, self).dispatch(*args, **kwargs)


class Indicator(DetailView):

    model = models.Indicator
    template_name = 'indicators/indicator.html'

    @method_decorator(auth.is_view_excluded('indicators'))
    def dispatch(self, *args, **kwargs):
        return super(Indicator, self).dispatch(*args, **kwargs)


class IndicatorCreate(CreateView):

    model = models.Indicator
    template_name = 'indicators/indicator_edit.html'

    @method_decorator(auth.is_view_excluded('indicators'))
    def dispatch(self, *args, **kwargs):
        return super(IndicatorCreate, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(IndicatorCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('indicators')
        return context


class IndicatorEdit(UpdateView):

    model = models.Indicator
    template_name = 'indicators/indicator_edit.html'

    @method_decorator(auth.is_view_excluded('indicators'))
    def dispatch(self, *args, **kwargs):
        return super(IndicatorEdit, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(IndicatorEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class IndicatorDelete(DeleteView):

    model = models.Indicator
    success_url = reverse_lazy('indicators')

    @method_decorator(auth.is_view_excluded('indicators'))
    def dispatch(self, *args, **kwargs):
        return super(IndicatorDelete, self).dispatch(*args, **kwargs)


class Trends(ListView):

    model = models.Trend
    template_name = 'trends/trends.html'
    paginate_by = PER_PAGE

    @method_decorator(auth.is_view_excluded('trends'))
    def dispatch(self, *args, **kwargs):
        return super(Trends, self).dispatch(*args, **kwargs)


class Trend(DetailView):

    model = models.Trend
    template_name = 'trends/trend.html'

    @method_decorator(auth.is_view_excluded('trend'))
    def dispatch(self, *args, **kwargs):
        return super(Trend, self).dispatch(*args, **kwargs)


class TrendCreate(CreateView):

    model = models.Trend
    template_name = 'trends/trend_edit.html'

    @method_decorator(auth.is_view_excluded('trend'))
    def dispatch(self, *args, **kwargs):
        return super(TrendCreate, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(TrendCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('trends')
        return context


class TrendEdit(UpdateView):

    model = models.Trend
    template_name = 'trends/trend_edit.html'

    @method_decorator(auth.is_view_excluded('trend'))
    def dispatch(self, *args, **kwargs):
        return super(TrendEdit, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(TrendEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class TrendDelete(DeleteView):

    model = models.Trend
    success_url = reverse_lazy('trends')

    @method_decorator(auth.is_view_excluded('trend'))
    def dispatch(self, *args, **kwargs):
        return super(TrendDelete, self).dispatch(*args, **kwargs)


# class GlobalTrends(ListView):

#     model = models.GlobalTrend
#     template_name = 'global_trends/global_trends.html'
#     paginate_by = PER_PAGE

#     @method_decorator(auth.is_view_excluded('global_trends'))
#     def dispatch(self, *args, **kwargs):
#         return super(GlobalTrends, self).dispatch(*args, **kwargs)


# class GlobalTrend(DetailView):

#     model = models.GlobalTrend
#     template_name = 'global_trends/global_trend.html'

#     @method_decorator(auth.is_view_excluded('global_trends'))
#     def dispatch(self, *args, **kwargs):
#         return super(GlobalTrend, self).dispatch(*args, **kwargs)


# class GlobalTrendCreate(CreateView):

#     model = models.GlobalTrend
#     template_name = 'global_trends/global_trend_edit.html'

#     @method_decorator(auth.is_view_excluded('global_trends'))
#     def dispatch(self, *args, **kwargs):
#         return super(GlobalTrendCreate, self).dispatch(*args, **kwargs)

#     def get_context_data(self, *args, **kwargs):
#         context = super(GlobalTrendCreate, self).get_context_data(*args, **kwargs)
#         context['cancel_url'] = reverse_lazy('global_trends')
#         return context


# class GlobalTrendEdit(UpdateView):

#     model = models.GlobalTrend
#     template_name = 'global_trends/global_trend_edit.html'

#     @method_decorator(auth.is_view_excluded('global_trends'))
#     def dispatch(self, *args, **kwargs):
#         return super(GlobalTrendEdit, self).dispatch(*args, **kwargs)

#     def get_context_data(self, *args, **kwargs):
#         context = super(GlobalTrendEdit, self).get_context_data(*args, **kwargs)
#         context['cancel_url'] = context['object'].get_absolute_url()
#         return context


# class GlobalTrendDelete(DeleteView):
#     model = models.GlobalTrend
#     success_url = reverse_lazy('global_trends')

#     @method_decorator(auth.is_view_excluded('global_trends'))
#     def dispatch(self, *args, **kwargs):
#         return super(GlobalTrendDelete, self).dispatch(*args, **kwargs)


class ThematicCategories(ListView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_categories.html'


class ThematicCategory(DetailView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ThematicCategory, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('trends')
        return context


class ThematicCategoryCreate(CreateView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ThematicCategoryCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('thematic_categories')
        return context


class ThematicCategoryEdit(UpdateView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ThematicCategoryEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class ThematicCategoryDelete(DeleteView):

    model = models.ThematicCategory
    success_url = reverse_lazy('thematic_categories')


class GeographicalScales(ListView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scales.html'


class GeographicalScale(DetailView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale.html'


class GeographicalScaleCreate(CreateView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalScaleCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('geographical_scales')
        return context

class GeographicalScaleEdit(UpdateView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalScaleEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GeographicalScaleDelete(DeleteView):

    model = models.GeographicalScale
    success_url = reverse_lazy('geographical_scales')


class GeographicalCoverages(ListView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverages.html'


class GeographicalCoverage(DetailView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage.html'


class GeographicalCoverageCreate(CreateView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalCoverageCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('geographical_coverages')
        return context


class GeographicalCoverageEdit(UpdateView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalCoverageEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GeographicalCoverageDelete(DeleteView):

    model = models.GeographicalCoverage
    success_url = reverse_lazy('geographical_coverages')



class SteepCategories(ListView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_categories.html'


class SteepCategory(DetailView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category.html'


class SteepCategoryCreate(CreateView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SteepCategoryCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('steep_categories')
        return context


class SteepCategoryEdit(UpdateView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SteepCategoryEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class SteepCategoryDelete(DeleteView):

    model = models.SteepCategory
    success_url = reverse_lazy('steep_categories')


class Timelines(ListView):

    model = models.Timeline
    template_name = 'timelines/timelines.html'


class Timeline(DetailView):

    model = models.Timeline
    template_name = 'timelines/timeline.html'


class TimelineCreate(CreateView):

    model = models.Timeline
    template_name = 'timelines/timeline_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TimelineCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse_lazy('timelines')
        return context


class TimelineEdit(UpdateView):

    model = models.Timeline
    template_name = 'timelines/timeline_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TimelineEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class TimelineDelete(DeleteView):

    model = models.Timeline
    success_url = reverse_lazy('timelines')
