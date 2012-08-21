import flatland as fl

from common import CommonString, SourceField

_SourcesSchema = fl.Dict.with_properties(widget="simple_schema").of(
    CommonString.named('short_name')
        .with_properties(label=u"Short name *",
                         not_empty_error=u"Please provide the short name")
        .using(optional=False),
    CommonString.named('long_name')
        .with_properties(label=u"Long name *",
                         not_empty_error=u"Please provide the long name")
        .using(optional=False),
    CommonString.named('year_of_publication')
        .with_properties(label=u"Year of publication *",
                         not_empty_error=u"Please provide the year of publication")
        .using(optional=False),
    CommonString.named('author')
        .with_properties(label=u"Author *",
                         not_empty_error=u"Please provide the author")
        .using(optional=False),
    CommonString.named('url')
        .with_properties(label=u"URL (to online availability) *",
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
        .with_properties(label=u"Code *",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description *",
                         not_empty_error=u"Please provide the description")
        .using(optional=False),
    SourceField.named('source')
        .with_properties(label=u"Source *",
                         not_empty_error=u"Please select the source")
        .using(optional=False, child_type=fl.Integer),
    CommonString.named('url')
        .with_properties(label=u"URL *",
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
        .with_properties(label=u"Code *",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description *",
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
        .with_properties(label=u"Code *",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description *",
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
        .with_properties(label=u"Code *",
                         not_empty_error=u"Please provide the code")
        .using(optional=False),
    CommonString.named('description')
        .with_properties(label=u"Description *",
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

