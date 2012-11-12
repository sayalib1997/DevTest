import json
from django.core.management.base import BaseCommand
from flis import models


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open(args[0]) as f:
            data = json.loads(f.read())

        for field, row in data['steep_categories'].items():
            models.SteepCategory.objects.create(**row)

        for field, row in data['geo_coverages'].items():
            models.GeographicalCoverage.objects.create(**row)

        for field, row in data['geo_scales'].items():
            models.GeographicalScale.objects.create(**row)

        for field, row in data['sources'].items():
            models.Source.objects.create(**row)

        for field, row in data['thematic_categories'].items():
            models.ThematicCategory.objects.create(**row)

        for field, row in data['timelines'].items():
            models.Timeline.objects.create(**row)

        for field, row in data['trends'].items():
            source = models.Source.objects.get(pk=row['source'])
            new_row = dict(row)
            new_row['source'] = source
            new_row.pop('url')
            models.Trend.objects.create(**new_row)

        for field, row in data['indicators'].items():
            row.pop('file_id', None)
            new_row = dict(row)
            new_row['source'] = models.Source.objects.get(pk=row['source'])
            new_row['geographic_coverage'] = models.GeographicalCoverage \
                .objects.get(pk=row['geo_coverage'])
            new_row.pop('geo_coverage')
            new_row['geographical_scale'] = models.GeographicalScale\
                .objects.get(pk=row['geo_scale'])
            new_row.pop('geo_scale')
            new_row['base_year'] = row['time_coverage_base_year']
            new_row['end_year'] = row['time_coverage_end_year']
            new_row.pop('time_coverage_base_year')
            new_row.pop('time_coverage_end_year')
            new_row['thematic_category'] = models.ThematicCategory\
                .objects.get(pk=row['thematic_category'])
            new_row['timeline'] = models.Timeline\
                .objects.get(pk=row['time_coverage_timeline'])
            new_row.pop('time_coverage_timeline')
            new_row.pop('url')
            models.Indicator.objects.create(**new_row)


        for field, row in data['gmts'].items():
            new_row = dict(row)
            new_row['source'] = models.Source.objects.get(pk=row['source'])
            new_row['steep_category'] = models.SteepCategory\
                .objects.get(pk=row['steep_category'])
            new_row.pop('url')
            models.GMT.objects.create(**new_row)

        for field, row in data['interlinks'].items():
            new_row = dict(row)
            new_row['gmt'] = models.GMT.objects.get(pk=row['gmt'])
            new_row['trend'] = models.Trend.objects.get(pk=row['trend'])

            if row['indicator1']:
                new_row['indicator_1'] = models.Indicator\
                    .objects.get(pk=row['indicator1'])

            if row['indicator2']:
                new_row['indicator_2'] = models.Indicator\
                    .objects.get(pk=row['indicator2'])

            if row['indicator3']:
                new_row['indicator_3'] = models.Indicator\
                    .objects.get(pk=row['indicator3'])

            if row['indicator4']:
                new_row['indicator_4'] = models.Indicator\
                    .objects.get(pk=row['indicator4'])

            new_row.pop('indicator1')
            new_row.pop('indicator2')
            new_row.pop('indicator3')
            new_row.pop('indicator4')
            models.Interlink.objects.create(**new_row)
