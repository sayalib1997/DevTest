import factory
from flis import models


class CountryFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Country


class ROCountryFactory(CountryFactory):

    iso = 'ro'
    name = 'Romania'


class SteepCategoryFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.SteepCategory

    code = factory.Sequence(lambda n: 'steep_category_{0}'.format(n))
    description = 'steep_category_description'


class SourceFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Source

    short_name = 'short_name'
    long_name = 'long_name'
    year_of_publication = 'year_of_publication'
    author = 'author'
    url = 'http://flis.dev'


class GMTFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.GMT

    code = factory.Sequence(lambda n: 'gmt_{0}'.format(n))
    steep_category = factory.SubFactory(SteepCategoryFactory)
    description = 'gmt_description'
    source = factory.SubFactory(SourceFactory)
    ownership = 'ownership'


class TrendFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Trend

    code = factory.Sequence(lambda n: 'trend_{0}'.format(n))
    description = 'trend_description'
    source = factory.SubFactory(SourceFactory)
    ownership = 'ownership'


class ThematicCategoryFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.ThematicCategory

    code = factory.Sequence(lambda n: 'thematic_categ_{0}'.format(n))
    description = 'thematic_categ_description'


class GeographicalScaleFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.GeographicalScale

    code = factory.Sequence(lambda n: 'geo_scale_{0}'.format(n))
    description = 'geo_scale_description'


class GeographicalCoverageFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.GeographicalCoverage

    code = factory.Sequence(lambda n: 'geo_coverage_{0}'.format(n))
    description = 'geo_coverage_description'


class TimelineFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Timeline

    title = 'timeline_factory'


class IndicatorFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Indicator

    code = factory.Sequence(lambda n: 'indicator_{0}'.format(n))
    description = 'indicator_description'
    thematic_category = factory.SubFactory(ThematicCategoryFactory)
    geographical_scale = factory.SubFactory(GeographicalScaleFactory)
    # geographical_coverage = factory.SubFactory(GeographicalCoverageFactory)
    timeline = factory.SubFactory(TimelineFactory)
    source = factory.SubFactory(SourceFactory)
    base_year = '2000'
    end_year = '2004'
    ownership = 'ownership'


class UncertaintyFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Uncertainty

    code = factory.Sequence(lambda n: 'uncertainty_{0}'.format(n))
    steep_category = factory.SubFactory(SteepCategoryFactory)
    description = 'uncertainty_description'
    source = factory.SubFactory(SourceFactory)
    ownership = 'ownership'


class InterlinkFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Interlink

    gmt = factory.SubFactory(GMTFactory)
    trend = factory.SubFactory(TrendFactory)
    uncertainty = factory.SubFactory(UncertaintyFactory)
    indicator_1 = factory.SubFactory(IndicatorFactory)
