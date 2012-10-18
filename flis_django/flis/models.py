from django.db import models
from django.core.urlresolvers import reverse


class Source(models.Model):

    short_name = models.CharField(max_length=512)
    long_name = models.CharField(max_length=512)
    year_of_publication = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    url = models.CharField(max_length=512)
    summary = models.TextField(null=True, blank=True, default='')

    def __unicode__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse('source_view', kwargs={'pk': self.pk})


class Trend(models.Model):

    source = models.ForeignKey(Source, related_name='sources_trend')
    code = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    url = models.CharField(max_length=512)
    ownership = models.CharField(max_length=512)
    summary = models.TextField(null=True, blank=True, default='')

    def get_absolute_url(self):
        return reverse('trend_view', kwargs={'pk': self.pk})


class ThematicCategory(models.Model):

    code = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def get_absolute_url(self):
        return reverse('thematic_category_view', kwargs={'pk': self.pk})


class GeographicalScale(models.Model):

    code = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def get_absolute_url(self):
        return reverse('geographical_scale_view', kwargs={'pk': self.pk})


class GeographicalCoverage(models.Model):

    code = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def get_absolute_url(self):
        return reverse('geographical_coverage_view', kwargs={'pk': self.pk})


class SteepCategory(models.Model):

    code = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def __unicode__(self):
        return '%s (%s)' % (self.code, self.description)

    def get_absolute_url(self):
        return reverse('steep_category_view', kwargs={'pk': self.pk})


class Timeline(models.Model):

    title = models.CharField(max_length=512)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('timeline_view', kwargs={'pk': self.pk})


class Indicator(models.Model):

    thematic_category = models.ForeignKey(ThematicCategory,
                                          related_name='thematic_category')
    geographical_scale = models.ForeignKey(GeographicalScale,
                                         related_name='geographical_scale')
    geographic_coverage = models.ForeignKey(GeographicalCoverage,
                                            related_name='geographic_coverage')
    timeline = models.ForeignKey(Timeline, related_name='timeline')
    source = models.ForeignKey(Source, related_name='sources_indicator')

    code = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    base_year = models.CharField(max_length=256)
    end_year = models.CharField(max_length=256)
    url = models.URLField(max_length=512)
    ownership = models.CharField(max_length=512)
    file_id = models.FileField(upload_to='indicator', max_length=256,
                               null=True, blank=True, default='')


class GMT(models.Model):

    steep_category = models.ForeignKey(SteepCategory,
                                       related_name='steep_category')
    source = models.ForeignKey(Source, related_name='sources_gmt')
    code = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    url = models.URLField(max_length=512)
    ownership = models.CharField(max_length=512)
    summary = models.TextField(null=True, blank=True, default='')


class Interlink(models.Model):

    gmt = models.ForeignKey(GMT, related_name='gmt')
    trend = models.ForeignKey(Trend, related_name='trend')
    indicator_1 = models.ForeignKey(Indicator, related_name='indicator_1')
    indicator_2 = models.ForeignKey(Indicator, related_name='indicator_2',
                                    null=True, blank=True)
    indicator_3 = models.ForeignKey(Indicator, related_name='indicator_3',
                                    null=True, blank=True)
    indicator_4 = models.ForeignKey(Indicator, related_name='indicator_4',
                                    null=True, blank=True)


