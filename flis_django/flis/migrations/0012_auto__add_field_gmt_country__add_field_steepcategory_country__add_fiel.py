# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GMT.country'
        db.add_column('flis_gmt', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'SteepCategory.country'
        db.add_column('flis_steepcategory', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'Source.country'
        db.add_column('flis_source', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'GeographicalScale.country'
        db.add_column('flis_geographicalscale', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'ThematicCategory.country'
        db.add_column('flis_thematiccategory', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'GeographicalCoverage.country'
        db.add_column('flis_geographicalcoverage', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'Trend.country'
        db.add_column('flis_trend', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'Interlink.country'
        db.add_column('flis_interlink', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'Timeline.country'
        db.add_column('flis_timeline', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))

        # Adding field 'Indicator.country'
        db.add_column('flis_indicator', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country']))


    def backwards(self, orm):
        # Deleting field 'GMT.country'
        db.delete_column('flis_gmt', 'country_id')

        # Deleting field 'SteepCategory.country'
        db.delete_column('flis_steepcategory', 'country_id')

        # Deleting field 'Source.country'
        db.delete_column('flis_source', 'country_id')

        # Deleting field 'GeographicalScale.country'
        db.delete_column('flis_geographicalscale', 'country_id')

        # Deleting field 'ThematicCategory.country'
        db.delete_column('flis_thematiccategory', 'country_id')

        # Deleting field 'GeographicalCoverage.country'
        db.delete_column('flis_geographicalcoverage', 'country_id')

        # Deleting field 'Trend.country'
        db.delete_column('flis_trend', 'country_id')

        # Deleting field 'Interlink.country'
        db.delete_column('flis_interlink', 'country_id')

        # Deleting field 'Timeline.country'
        db.delete_column('flis_timeline', 'country_id')

        # Deleting field 'Indicator.country'
        db.delete_column('flis_indicator', 'country_id')


    models = {
        'flis.country': {
            'Meta': {'object_name': 'Country'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'flis.geographicalcoverage': {
            'Meta': {'object_name': 'GeographicalCoverage'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.geographicalscale': {
            'Meta': {'object_name': 'GeographicalScale'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.gmt': {
            'Meta': {'object_name': 'GMT'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
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
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'end_year': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'geographical_coverage': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Indicators'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.GeographicalCoverage']"}),
            'geographical_scale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Indicators'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.GeographicalScale']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources_indicator'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'thematic_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Indicators'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.ThematicCategory']"}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'timeline'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Timeline']"})
        },
        'flis.interlink': {
            'Meta': {'object_name': 'Interlink'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
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
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
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
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.thematiccategory': {
            'Meta': {'object_name': 'ThematicCategory'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'flis.trend': {
            'Meta': {'object_name': 'Trend'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trends'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['flis']