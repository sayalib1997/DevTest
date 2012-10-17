from django.conf.urls import patterns, include, url
from flis import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', views.Home.as_view(), name='home'),

    url(r'^sources$', views.Sources.as_view(), name='sources'),
    url(r'^sources/new$', views.SourceCreate.as_view(), name='source_new'),
    url(r'^sources/(?P<pk>\d+)/edit$', views.SourceEdit.as_view(), name='source_edit'),
    url(r'^sources/(?P<pk>\d+)/$', views.Source.as_view(), name='source_view'),
    url(r'^sources/(?P<pk>\d+)/delete$', views.SourceDelete.as_view(), name='source_delete'),

    url(r'^settings/trends$', views.Trends.as_view(), name='trends'),
    url(r'^settings/trends/new$', views.TrendCreate.as_view(), name='trend_new'),
    url(r'^settings/trends/(?P<pk>\d+)/edit$', views.TrendEdit.as_view(), name='trend_edit'),
    url(r'^settings/trends/(?P<pk>\d+)/$', views.Trend.as_view(), name='trend_view'),
    url(r'^settings/trends/(?P<pk>\d+)/delete$', views.TrendDelete.as_view(), name='trend_delete'),

    url(r'^settings/thematic_categories$', views.ThematicCategories.as_view(), name='thematic_categories'),
    url(r'^settings/thematic_categories/new$', views.ThematicCategoryCreate.as_view(), name='thematic_category_new'),
    url(r'^settings/thematic_categories/(?P<pk>\d+)/edit$', views.ThematicCategoryEdit.as_view(), name='thematic_category_edit'),
    url(r'^settings/thematic_categories/(?P<pk>\d+)/$', views.ThematicCategory.as_view(), name='thematic_category_view'),
    url(r'^settings/thematic_categories/(?P<pk>\d+)/delete$', views.ThematicCategoryDelete.as_view(), name='thematic_category_delete'),

    url(r'^settings/geographical_scales$', views.GeographicalScales.as_view(), name='geographical_scales'),
    url(r'^settings/geographical_scales/new$', views.GeographicalScaleCreate.as_view(), name='geographical_scale_new'),
    url(r'^settings/geographical_scales/(?P<pk>\d+)/edit$', views.GeographicalScaleEdit.as_view(), name='geographical_scale_edit'),
    url(r'^settings/geographical_scales/(?P<pk>\d+)/$', views.GeographicalScale.as_view(), name='geographical_scale_view'),
    url(r'^settings/geographical_scales/(?P<pk>\d+)/delete$', views.GeographicalScaleDelete.as_view(), name='geographical_scale_delete'),


    url(r'^settings/geographical_coverages$', views.GeographicalCoverages.as_view(), name='geographical_coverages'),
    url(r'^settings/geographical_coverages/new$', views.GeographicalCoverageCreate.as_view(), name='geographical_coverage_new'),
    url(r'^settings/geographical_coverages/(?P<pk>\d+)/edit$', views.GeographicalCoverageEdit.as_view(), name='geographical_coverage_edit'),
    url(r'^settings/geographical_coverages/(?P<pk>\d+)/$', views.GeographicalCoverage.as_view(), name='geographical_coverage_view'),
    url(r'^settings/geographical_coverages/(?P<pk>\d+)/delete$', views.GeographicalCoverageDelete.as_view(), name='geographical_coverage_delete'),

    url(r'^settings/steep_categories$', views.SteepCategories.as_view(), name='steep_categories'),
    url(r'^settings/steep_categories/new$', views.SteepCategoryCreate.as_view(), name='steep_category_new'),
    url(r'^settings/steep_categories/(?P<pk>\d+)/edit$', views.SteepCategoryEdit.as_view(), name='steep_category_edit'),
    url(r'^settings/steep_categories/(?P<pk>\d+)/$', views.SteepCategory.as_view(), name='steep_category_view'),
    url(r'^settings/steep_categories/(?P<pk>\d+)/delete$', views.SteepCategoryDelete.as_view(), name='steep_category_delete'),

    url(r'^settings/timelines$', views.Timelines.as_view(), name='timelines'),
    url(r'^settings/timelines/new$', views.TimelineCreate.as_view(), name='timeline_new'),
    url(r'^settings/timelines/(?P<pk>\d+)/edit$', views.TimelineEdit.as_view(), name='timeline_edit'),
    url(r'^settings/timelines/(?P<pk>\d+)/$', views.Timeline.as_view(), name='timeline_view'),
    url(r'^settings/timelines/(?P<pk>\d+)/delete$', views.TimelineDelete.as_view(), name='timeline_delete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
