from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from flis import views, auth

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

flis_patterns = patterns('',

    url(r'^$', views.Interlinks.as_view(), name='interlinks'),

    url(r'^interlinks/new/$',
        auth.edit_is_allowed(views.InterlinkCreate.as_view()),
        name='interlink_new'),

    url(r'^interlinks/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.InterlinkEdit.as_view()),
        name='interlink_edit'),

    url(r'^interlinks/(?P<pk>\d+)/$', views.Interlink.as_view(), name='interlink_view'),

    url(r'^interlinks/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.InterlinkDelete.as_view()),
        name='interlink_delete'),

    url(r'^sources/$', views.Sources.as_view(), name='sources'),

    url(r'^sources/new/$',
        auth.edit_is_allowed(views.SourceCreate.as_view()),
        name='source_new'),

    url(r'^sources/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.SourceEdit.as_view()),
        name='source_edit'),

    url(r'^sources/(?P<pk>\d+)/$', views.Source.as_view(), name='source_view'),

    url(r'^sources/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.SourceDelete.as_view()),
        name='source_delete'),

    url(r'^indicators/$', views.Indicators.as_view(), name='indicators'),

    url(r'^indicators/new/$',
        auth.edit_is_allowed(views.IndicatorCreate.as_view()),
        name='indicator_new'),

    url(r'^indicators/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.IndicatorEdit.as_view()),
        name='indicator_edit'),

    url(r'^indicators/(?P<pk>\d+)/$', views.Indicator.as_view(), name='indicator_view'),

    url(r'^indicators/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.IndicatorDelete.as_view()),
        name='indicator_delete'),

#GMTs
    url(r'^gmts/$', views.GMTs.as_view(), name='gmts'),

    url(r'^gmts/new/$',
        auth.edit_is_allowed(views.GMTCreate.as_view()),
        name='gmt_new'),

    url(r'^gmts/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.GMTEdit.as_view()),
        name='gmt_edit'),

    url(r'^gmts/(?P<pk>\d+)/$', views.GMT.as_view(), name='gmt_view'),

    url(r'^gmts/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.GMTDelete.as_view()),
        name='gmt_delete'),

#Models
    url(r'^flismodels/$', views.FlisModels.as_view(), name='flismodels'),

    url(r'^flismodels/new/$',
        auth.edit_is_allowed(views.FlisModelCreate.as_view()),
        name='flismodel_new'),

    url(r'^flismodels/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.FlisModelEdit.as_view()),
        name='flismodel_edit'),

    url(r'^flismodels/(?P<pk>\d+)/$', views.FlisModel.as_view(), name='flismodel_view'),

    url(r'^flismodels/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.FlisModelDelete.as_view()),
        name='flismodel_delete'),

#Horizon scanning
    url(r'^horizonscannings/$', views.HorizonScannings.as_view(), name='horizonscannings'),

    url(r'^horizonscannings/new/$',
        auth.edit_is_allowed(views.HorizonScanningCreate.as_view()),
        name='horizonscanning_new'),

    url(r'^horizonscannings/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.HorizonScanningEdit.as_view()),
        name='horizonscanning_edit'),

    url(r'^horizonscannings/(?P<pk>\d+)/$', views.HorizonScanning.as_view(), name='horizonscanning_view'),

    url(r'^horizonscannings/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.HorizonScanningDelete.as_view()),
        name='horizonscanning_delete'),

#Methods and tools
    url(r'^methodstools/$', views.MethodsTools.as_view(), name='methodstools'),

    url(r'^methodstools/new/$',
        auth.edit_is_allowed(views.MethodToolCreate.as_view()),
        name='methodtool_new'),

    url(r'^methodstools/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.MethodToolEdit.as_view()),
        name='methodtool_edit'),

    url(r'^methodstools/(?P<pk>\d+)/$', views.MethodTool.as_view(), name='methodtool_view'),

    url(r'^methodstools/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.MethodToolDelete.as_view()),
        name='methodtool_delete'),

#Uncertainties
    url(r'^uncertainties/$', views.Uncertainties.as_view(), name='uncertainties'),

    url(r'^uncertainties/new/$',
        auth.edit_is_allowed(views.UncertaintyCreate.as_view()),
        name='uncertainty_new'),

    url(r'^uncertainties/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.UncertaintyEdit.as_view()),
        name='uncertainty_edit'),

    url(r'^uncertainties/(?P<pk>\d+)/$', views.Uncertainty.as_view(), name='uncertainty_view'),

    url(r'^uncertainties/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.UncertaintyDelete.as_view()),
        name='uncertainty_delete'),

#Wild cards
    url(r'^wildcards/$', views.WildCards.as_view(), name='wildcards'),

    url(r'^wildcards/new/$',
        auth.edit_is_allowed(views.WildCardCreate.as_view()),
        name='wildcard_new'),

    url(r'^wildcards/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.WildCardEdit.as_view()),
        name='wildcard_edit'),

    url(r'^wildcards/(?P<pk>\d+)/$', views.WildCard.as_view(), name='wildcard_view'),

    url(r'^wildcards/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.WildCardDelete.as_view()),
        name='wildcard_delete'),

#Early warnings
    url(r'^earlywarnings/$', views.EarlyWarnings.as_view(), name='earlywarnings'),

    url(r'^earlywarnings/new/$',
        auth.edit_is_allowed(views.EarlyWarningCreate.as_view()),
        name='earlywarning_new'),

    url(r'^earlywarnings/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.EarlyWarningEdit.as_view()),
        name='earlywarning_edit'),

    url(r'^earlywarnings/(?P<pk>\d+)/$', views.EarlyWarning.as_view(), name='earlywarning_view'),

    url(r'^earlywarnings/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.EarlyWarningDelete.as_view()),
        name='earlywarning_delete'),

#Trends
    url(r'^trends/$', views.Trends.as_view(), name='trends'),

    url(r'^trends/new/$',
        auth.edit_is_allowed(views.TrendCreate.as_view()),
        name='trend_new'),

    url(r'^trends/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.TrendEdit.as_view()),
        name='trend_edit'),

    url(r'^trends/(?P<pk>\d+)/$', views.Trend.as_view(), name='trend_view'),

    url(r'^trends/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.TrendDelete.as_view()),
        name='trend_delete'),

#Blossom
    url(r'^blossoms/$', views.Blossoms.as_view(), name='blossoms'),

    url(r'^blossoms/new/$',
        auth.edit_is_allowed(views.BlossomCreate.as_view()),
        name='blossom_new'),

    url(r'^blossoms/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.BlossomEdit.as_view()),
        name='blossom_edit'),

    url(r'^blossoms/(?P<pk>\d+)/$', views.Blossom.as_view(), name='blossom_view'),

    url(r'^blossoms/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.BlossomDelete.as_view()),
        name='blossom_delete'),

#Thematic categories
    url(r'^settings/thematic_categories/$', views.ThematicCategories.as_view(), name='thematic_categories'),

    url(r'^settings/thematic_categories/new/$',
        auth.edit_is_allowed(views.ThematicCategoryCreate.as_view()),
        name='thematic_category_new'),

    url(r'^settings/thematic_categories/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.ThematicCategoryEdit.as_view()),
        name='thematic_category_edit'),

    url(r'^settings/thematic_categories/(?P<pk>\d+)/$', views.ThematicCategory.as_view(), name='thematic_category_view'),

    url(r'^settings/thematic_categories/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.ThematicCategoryDelete.as_view()),
        name='thematic_category_delete'),

#Geographical scales
    url(r'^settings/geographical_scales/$', views.GeographicalScales.as_view(), name='geographical_scales'),

    url(r'^settings/geographical_scales/new/$',
        auth.edit_is_allowed(views.GeographicalScaleCreate.as_view()),
        name='geographical_scale_new'),

    url(r'^settings/geographical_scales/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.GeographicalScaleEdit.as_view()),
        name='geographical_scale_edit'),

    url(r'^settings/geographical_scales/(?P<pk>\d+)/$', views.GeographicalScale.as_view(), name='geographical_scale_view'),

    url(r'^settings/geographical_scales/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.GeographicalScaleDelete.as_view()),
        name='geographical_scale_delete'),

#scenarios
    url(r'^settings/scenarios/$', views.Scenarios.as_view(),
        name='scenarios'),

    url(r'^settings/scenarios/new/$',
        auth.edit_is_allowed(views.ScenarioCreate.as_view()),
        name='scenario_new'),

    url(r'^settings/scenarios/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.ScenarioEdit.as_view()),
        name='scenario_edit'),

    url(r'^settings/scenarios/(?P<pk>\d+)/$', views.Scenario.as_view(), name='scenario_view'),

    url(r'^settings/scenarios/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.ScenarioDelete.as_view()),
        name='scenario_delete'),

#geographical coverage
    url(r'^settings/geographical_coverages/$', views.GeographicalCoverages.as_view(), name='geographical_coverages'),

    url(r'^settings/geographical_coverages/new/$',
        auth.edit_is_allowed(views.GeographicalCoverageCreate.as_view()),
        name='geographical_coverage_new'),

    url(r'^settings/geographical_coverages/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.GeographicalCoverageEdit.as_view()),
        name='geographical_coverage_edit'),

    url(r'^settings/geographical_coverages/(?P<pk>\d+)/$', views.GeographicalCoverage.as_view(), name='geographical_coverage_view'),

    url(r'^settings/geographical_coverages/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.GeographicalCoverageDelete.as_view()),
        name='geographical_coverage_delete'),

    url(r'^settings/steep_categories/$', views.SteepCategories.as_view(), name='steep_categories'),

    url(r'^settings/steep_categories/new/$',
        auth.edit_is_allowed(views.SteepCategoryCreate.as_view()),
        name='steep_category_new'),

    url(r'^settings/steep_categories/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.SteepCategoryEdit.as_view()),
        name='steep_category_edit'),

    url(r'^settings/steep_categories/(?P<pk>\d+)/$', views.SteepCategory.as_view(), name='steep_category_view'),

    url(r'^settings/steep_categories/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.SteepCategoryDelete.as_view()),
        name='steep_category_delete'),

    url(r'^settings/timelines/$', views.Timelines.as_view(), name='timelines'),

    url(r'^settings/timelines/new/$',
        auth.edit_is_allowed(views.TimelineCreate.as_view()),
        name='timeline_new'),

    url(r'^settings/timelines/(?P<pk>\d+)/edit/$',
        auth.edit_is_allowed(views.TimelineEdit.as_view()),
        name='timeline_edit'),

    url(r'^settings/timelines/(?P<pk>\d+)/$', views.Timeline.as_view(), name='timeline_view'),

    url(r'^settings/timelines/(?P<pk>\d+)/delete/$',
        auth.edit_is_allowed(views.TimelineDelete.as_view()),
        name='timeline_delete'),

)

urlpatterns = patterns('',

    url(r'^management/', include(admin.site.urls)),

    url(r'^(?P<country>[-\w]+)/', include(flis_patterns)),

)
