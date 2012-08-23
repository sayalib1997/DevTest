import flatland as fl
import flask
from werkzeug import secure_filename
import database

from common import (CommonString, CommonDict ,SourceField,
                    ThematicCategoryField, GeoScaleField, GeoCoverageField,
                    TimelineField, SteepCategoryField)

_GMTsSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('code')
        .with_properties(label=u"Code",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    SteepCategoryField.named('steep_category')
        .with_properties(label=u"Steep category",
                         not_empty_error=u"Please select the steep category")
        .using(optional=False, child_type=fl.Integer),
    CommonString.named('description')
        .with_properties(label=u"Description",
                         not_empty_error=u"Please provide the description")
        .using(optional=False),
    SourceField.named('source')
        .with_properties(label=u"Source",
                         not_empty_error=u"Please select the source")
        .using(optional=False, child_type=fl.Integer),
    CommonString.named('url')
        .with_properties(label=u"URL",
                         not_empty_error=(u"Please provide the URL "
                             u"(to published GMT brief)"))
        .using(optional=False),
    CommonString.named('ownership')
        .with_properties(label=u"Ownership*",
                         not_empty_error=u"Please provide the ownership")
        .using(optional=False),
    CommonString.named('summary')
        .with_properties(widget='textarea', label=u"Summary"),
)

class GMTsSchema(_GMTsSchema):

    @property
    def value(self):
        return GMT(super(GMTsSchema, self).value)

class GMT(dict):

    id = None

    @staticmethod
    def from_flat(gmts_row):
        gmt = GMTsSchema.from_flat(gmts_row)

        gmt = gmt.value
        gmt.id = gmts_row.id

        return gmt


_SourcesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('short_name')
        .with_properties(label=u"Short name",
                         not_empty_error=u"Please provide the short name")
        .using(optional=False),
    CommonString.named('long_name')
        .with_properties(label=u"Long name",
                         not_empty_error=u"Please provide the long name")
        .using(optional=False),
    CommonString.named('year_of_publication')
        .with_properties(label=u"Year of publication",
                         not_empty_error=u"Please provide the year of publication")
        .using(optional=False),
    CommonString.named('author')
        .with_properties(label=u"Author",
                         not_empty_error=u"Please provide the author")
        .using(optional=False),
    CommonString.named('url')
        .with_properties(label=u"URL (to online availability)",
                         not_empty_error=u"Please provide the URL")
        .using(optional=False),
    CommonString.named('summary')
        .with_properties(widget='textarea', label=u"Summary"),
)

class SourcesSchema(_SourcesSchema):

    @property
    def value(self):
        return Source(super(SourcesSchema, self).value)

class Source(dict):

    id = None

    @staticmethod
    def from_flat(sources_row):
        source = SourcesSchema.from_flat(sources_row)

        source = source.value
        source.id = sources_row.id

        return source


_TrendsSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('code')
        .with_properties(label=u"Code",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description",
                         not_empty_error=u"Please provide the description")
        .using(optional=False),
    SourceField.named('source')
        .with_properties(label=u"Source",
                         not_empty_error=u"Please select the source")
        .using(optional=False, child_type=fl.Integer),
    CommonString.named('url')
        .with_properties(label=u"URL",
                         not_empty_error=(u"Please provide the URL "
                             u"(to published GMT brief)"))
        .using(optional=False),
    CommonString.named('ownership')
        .with_properties(label=u"Ownership*",
                         not_empty_error=u"Please provide the ownership")
        .using(optional=False),
    CommonString.named('summary')
        .with_properties(widget='textarea', label=u"Summary"),
)

class TrendsSchema(_TrendsSchema):

    @property
    def value(self):
        return Trend(super(TrendsSchema, self).value)

class Trend(dict):

    id = None

    @staticmethod
    def from_flat(trends_row):
        trend = TrendsSchema.from_flat(trends_row)

        trend = trend.value
        trend.id = trends_row.id

        return trend

_ThematicCategoriesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('code')
        .with_properties(label=u"Code",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description",
                         not_empty_error=u"Please provide the description")
        .using(optional=False),
)

class ThematicCategoriesSchema(_ThematicCategoriesSchema):

    @property
    def value(self):
        return Trend(super(ThematicCategoriesSchema, self).value)

class ThematicCategory(dict):

    id = None

    @staticmethod
    def from_flat(thematic_categories_row):
        thematic_category = ThematicCategoriesSchema.from_flat(
                thematic_categories_row)

        thematic_category = thematic_category.value
        thematic_category.id = thematic_categories_row.id

        return thematic_category

_GeographicalScalesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('code')
        .with_properties(label=u"Code",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description",
                         not_empty_error=u"Please provide the description")
        .using(optional=False),
)

class GeographicalScalesSchema(_GeographicalScalesSchema):

    @property
    def value(self):
        return Trend(super(GeographicalScalesSchema, self).value)

class GeographicalScale(dict):

    id = None

    @staticmethod
    def from_flat(geographical_scales_row):
        geographical_scale = GeographicalScalesSchema.from_flat(
                geographical_scales_row)

        geographical_scale = geographical_scale.value
        geographical_scale.id = geographical_scales_row.id

        return geographical_scale

_GeographicalCoveragesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('code')
        .with_properties(label=u"Code",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description",
                         not_empty_error=u"Please provide the description")
        .using(optional=False),
)

class GeographicalCoveragesSchema(_GeographicalCoveragesSchema):

    @property
    def value(self):
        return Trend(super(GeographicalCoveragesSchema, self).value)

class GeographicalCoverage(dict):

    id = None

    @staticmethod
    def from_flat(geographical_coverages_row):
        geographical_coverage = GeographicalCoveragesSchema.from_flat(
                geographical_coverages_row)

        geographical_coverage = geographical_coverage.value
        geographical_coverage.id = geographical_coverages_row.id

        return geographical_coverage

_SteepCategoriesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('code')
        .with_properties(label=u"Code",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description",
                         not_empty_error=u"Please provide the description")
        .using(optional=False),
)

class SteepCategoriesSchema(_SteepCategoriesSchema):

    @property
    def value(self):
        return Trend(super(SteepCategoriesSchema, self).value)

class SteepCategory(dict):

    id = None

    @staticmethod
    def from_flat(steep_categories_row):
        steep_category = SteepCategoriesSchema.from_flat(
                steep_categories_row)

        steep_category = steep_category.value
        steep_category.id = steep_categories_row.id

        return steep_category

_TimelinesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('title')
        .with_properties(label=u"Title",
                         not_empty_error=u"Please provide the title")
        .using(optional=False),
)

class TimelinesSchema(_TimelinesSchema):

    @property
    def value(self):
        return Timeline(super(TimelinesSchema, self).value)

class Timeline(dict):

    id = None

    @staticmethod
    def from_flat(timelines_row):
        timeline = TimelinesSchema.from_flat(timelines_row)

        timeline = timeline.value
        timeline.id = timelines_row.id

        return timeline

_IndicatorsSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('code')
        .with_properties(label=u"Code",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    ThematicCategoryField.named('thematic_category')
        .with_properties(label=u"Thematic category",
                         not_empty_error=u"Please select the thematic category")
        .using(optional=False, child_type=fl.Integer),
    CommonString.named('description')
        .with_properties(label=u"Description",
                         not_empty_error=u"Please provide the description")
        .using(optional=False),
    GeoScaleField.named('geographical_scale')
        .with_properties(label=u"Geo scale",
                         not_empty_error=u"Please select the geo scale")
        .using(optional=False, child_type=fl.Integer),
    GeoCoverageField.named('geographical_coverage')
        .with_properties(label=u"Geo coverage",
                         not_empty_error=u"Please select the geo coverage")
        .using(optional=False, child_type=fl.Integer),

    CommonDict.named("time_coverage")
              .with_properties(label=u"Time coverage")
              .of(
        CommonString.named('base_year')
            .with_properties(label=u"Base year",
                             not_empty_error=u"Please provide the base year ")
            .using(optional=False),
        CommonString.named('end_year')
            .with_properties(label=u"End year",
                             not_empty_error=u"Please provide the end year")
            .using(optional=False),
        TimelineField.named('timeline')
            .with_properties(label=u"Timeline",
                             not_empty_error=u"Please select the timeline")
            .using(optional=False, child_type=fl.Integer),
    ),

    SourceField.named('source')
        .with_properties(label=u"Source",
                         not_empty_error=u"Please select the source")
        .using(optional=False, child_type=fl.Integer),
    CommonString.named('url')
        .with_properties(label=u"URL",
                         not_empty_error=u"Please provide the URL")
        .using(optional=False),
    CommonString.named('ownership')
        .with_properties(label=u"Ownership",
                         not_empty_error=u"Please provide the ownership")
        .using(optional=False),
    CommonString.named("file_id")
                 .using(label="", optional=True)
                 .with_properties(widget="file", label=u"Example of file"),

)

class IndicatorsSchema(_IndicatorsSchema):

    @property
    def value(self):
        return Indicator(super(IndicatorsSchema, self).value)

class Indicator(dict):

    id = None

    @staticmethod
    def from_flat(indicators_row):
        indicator = IndicatorsSchema.from_flat(indicators_row)

        indicator = indicator.value
        indicator.id = indicators_row.id

        return indicator

    @property
    def has_file(self):
        assert self.id is not None
        indicator_row = database.get_or_404("indicators", self.id)
        return bool(indicator_row.get("file_id", ""))

    @property
    def file(self):
        if self["file_id"]:
          filename = "files/%s" % self["file_id"]
          return flask.url_for("static", filename=filename)
        else:
          return None

