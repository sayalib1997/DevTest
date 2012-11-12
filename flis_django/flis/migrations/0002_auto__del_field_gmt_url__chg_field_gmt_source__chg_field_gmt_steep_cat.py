# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'GMT.url'
        db.delete_column('flis_gmt', 'url')


        # Changing field 'GMT.source'
        db.alter_column('flis_gmt', 'source_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['flis.Source']))

        # Changing field 'GMT.steep_category'
        db.alter_column('flis_gmt', 'steep_category_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.PROTECT, to=orm['flis.SteepCategory']))
        # Deleting field 'Trend.url'
        db.delete_column('flis_trend', 'url')


        # Changing field 'Trend.source'
        db.alter_column('flis_trend', 'source_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['flis.Source']))

        # Changing field 'Interlink.indicator_1'
        db.alter_column('flis_interlink', 'indicator_1_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['flis.Indicator']))

        # Changing field 'Interlink.indicator_3'
        db.alter_column('flis_interlink', 'indicator_3_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.PROTECT, to=orm['flis.Indicator']))

        # Changing field 'Interlink.indicator_2'
        db.alter_column('flis_interlink', 'indicator_2_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.PROTECT, to=orm['flis.Indicator']))

        # Changing field 'Interlink.indicator_4'
        db.alter_column('flis_interlink', 'indicator_4_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.PROTECT, to=orm['flis.Indicator']))

        # Changing field 'Interlink.trend'
        db.alter_column('flis_interlink', 'trend_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['flis.Trend']))
        # Deleting field 'Indicator.url'
        db.delete_column('flis_indicator', 'url')


        # Changing field 'Indicator.geographic_coverage'
        db.alter_column('flis_indicator', 'geographic_coverage_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.PROTECT, to=orm['flis.GeographicalCoverage']))

        # Changing field 'Indicator.timeline'
        db.alter_column('flis_indicator', 'timeline_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['flis.Timeline']))

        # Changing field 'Indicator.geographical_scale'
        db.alter_column('flis_indicator', 'geographical_scale_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.PROTECT, to=orm['flis.GeographicalScale']))

        # Changing field 'Indicator.thematic_category'
        db.alter_column('flis_indicator', 'thematic_category_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['flis.ThematicCategory']))

        # Changing field 'Indicator.source'
        db.alter_column('flis_indicator', 'source_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['flis.Source']))

    def backwards(self, orm):
        # Adding field 'GMT.url'
        db.add_column('flis_gmt', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=512),
                      keep_default=False)


        # Changing field 'GMT.source'
        db.alter_column('flis_gmt', 'source_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Source']))

        # Changing field 'GMT.steep_category'
        db.alter_column('flis_gmt', 'steep_category_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['flis.SteepCategory']))
        # Adding field 'Trend.url'
        db.add_column('flis_trend', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=512),
                      keep_default=False)


        # Changing field 'Trend.source'
        db.alter_column('flis_trend', 'source_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Source']))

        # Changing field 'Interlink.indicator_1'
        db.alter_column('flis_interlink', 'indicator_1_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Indicator']))

        # Changing field 'Interlink.indicator_3'
        db.alter_column('flis_interlink', 'indicator_3_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['flis.Indicator']))

        # Changing field 'Interlink.indicator_2'
        db.alter_column('flis_interlink', 'indicator_2_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['flis.Indicator']))

        # Changing field 'Interlink.indicator_4'
        db.alter_column('flis_interlink', 'indicator_4_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['flis.Indicator']))

        # Changing field 'Interlink.trend'
        db.alter_column('flis_interlink', 'trend_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Trend']))
        # Adding field 'Indicator.url'
        db.add_column('flis_indicator', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=512),
                      keep_default=False)


        # Changing field 'Indicator.geographic_coverage'
        db.alter_column('flis_indicator', 'geographic_coverage_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['flis.GeographicalCoverage']))

        # Changing field 'Indicator.timeline'
        db.alter_column('flis_indicator', 'timeline_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Timeline']))

        # Changing field 'Indicator.geographical_scale'
        db.alter_column('flis_indicator', 'geographical_scale_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['flis.GeographicalScale']))

        # Changing field 'Indicator.thematic_category'
        db.alter_column('flis_indicator', 'thematic_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.ThematicCategory']))

        # Changing field 'Indicator.source'
        db.alter_column('flis_indicator', 'source_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Source']))

    models = {
        'flis.geographicalcoverage': {
            'Meta': {'object_name': 'GeographicalCoverage'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.geographicalscale': {
            'Meta': {'object_name': 'GeographicalScale'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.gmt': {
            'Meta': {'object_name': 'GMT'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gmts'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gmts'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'base_year': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'end_year': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'geographic_coverage': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Indicators'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.GeographicalCoverage']"}),
            'geographical_scale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Indicators'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.GeographicalScale']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources_indicator'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'thematic_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Indicators'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.ThematicCategory']"}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'timeline'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Timeline']"})
        },
        'flis.interlink': {
            'Meta': {'object_name': 'Interlink'},
            'gmt': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interlinks'", 'to': "orm['flis.GMT']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicator_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interlinks_indicator_1'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Indicator']"}),
            'indicator_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'interlinks_indicator_2'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.Indicator']"}),
            'indicator_3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'interlinks_indicator_3'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.Indicator']"}),
            'indicator_4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'interlinks_indicator_4'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.Indicator']"}),
            'trend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interlinks'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Trend']"})
        },
        'flis.source': {
            'Meta': {'object_name': 'Source'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'year_of_publication': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'flis.steepcategory': {
            'Meta': {'object_name': 'SteepCategory'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.thematiccategory': {
            'Meta': {'object_name': 'ThematicCategory'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'flis.trend': {
            'Meta': {'object_name': 'Trend'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trends'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['flis']