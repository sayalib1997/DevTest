# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Source'
        db.create_table('flis_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('long_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('year_of_publication', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['Source'])

        # Adding model 'Trend'
        db.create_table('flis_trend', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sources_trend', to=orm['flis.Source'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['Trend'])

        # Adding model 'ThematicCategory'
        db.create_table('flis_thematiccategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('flis', ['ThematicCategory'])

        # Adding model 'GeographicalScale'
        db.create_table('flis_geographicalscale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('flis', ['GeographicalScale'])

        # Adding model 'GeographicalCoverage'
        db.create_table('flis_geographicalcoverage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('flis', ['GeographicalCoverage'])

        # Adding model 'SteepCategory'
        db.create_table('flis_steepcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('flis', ['SteepCategory'])

        # Adding model 'Timeline'
        db.create_table('flis_timeline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('flis', ['Timeline'])

        # Adding model 'Indicator'
        db.create_table('flis_indicator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('thematic_category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='thematic_category', to=orm['flis.ThematicCategory'])),
            ('geographical_scale', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geographical_scale', null=True, to=orm['flis.GeographicalScale'])),
            ('geographic_coverage', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='geographic_coverage', null=True, to=orm['flis.GeographicalCoverage'])),
            ('timeline', self.gf('django.db.models.fields.related.ForeignKey')(related_name='timeline', to=orm['flis.Timeline'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sources_indicator', to=orm['flis.Source'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('base_year', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('end_year', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['Indicator'])

        # Adding model 'GMT'
        db.create_table('flis_gmt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('steep_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='steep_category', null=True, to=orm['flis.SteepCategory'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sources_gmt', to=orm['flis.Source'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['GMT'])

        # Adding model 'Interlink'
        db.create_table('flis_interlink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gmt', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gmt', to=orm['flis.GMT'])),
            ('trend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trend', to=orm['flis.Trend'])),
            ('indicator_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicator_1', to=orm['flis.Indicator'])),
            ('indicator_2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicator_2', null=True, to=orm['flis.Indicator'])),
            ('indicator_3', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicator_3', null=True, to=orm['flis.Indicator'])),
            ('indicator_4', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicator_4', null=True, to=orm['flis.Indicator'])),
        ))
        db.send_create_signal('flis', ['Interlink'])


    def backwards(self, orm):
        # Deleting model 'Source'
        db.delete_table('flis_source')

        # Deleting model 'Trend'
        db.delete_table('flis_trend')

        # Deleting model 'ThematicCategory'
        db.delete_table('flis_thematiccategory')

        # Deleting model 'GeographicalScale'
        db.delete_table('flis_geographicalscale')

        # Deleting model 'GeographicalCoverage'
        db.delete_table('flis_geographicalcoverage')

        # Deleting model 'SteepCategory'
        db.delete_table('flis_steepcategory')

        # Deleting model 'Timeline'
        db.delete_table('flis_timeline')

        # Deleting model 'Indicator'
        db.delete_table('flis_indicator')

        # Deleting model 'GMT'
        db.delete_table('flis_gmt')

        # Deleting model 'Interlink'
        db.delete_table('flis_interlink')


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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources_gmt'", 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'steep_category'", 'null': 'True', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512'})
        },
        'flis.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'base_year': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'end_year': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'geographic_coverage': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geographic_coverage'", 'null': 'True', 'to': "orm['flis.GeographicalCoverage']"}),
            'geographical_scale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geographical_scale'", 'null': 'True', 'to': "orm['flis.GeographicalScale']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources_indicator'", 'to': "orm['flis.Source']"}),
            'thematic_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thematic_category'", 'to': "orm['flis.ThematicCategory']"}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'timeline'", 'to': "orm['flis.Timeline']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512'})
        },
        'flis.interlink': {
            'Meta': {'object_name': 'Interlink'},
            'gmt': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gmt'", 'to': "orm['flis.GMT']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicator_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'indicator_1'", 'to': "orm['flis.Indicator']"}),
            'indicator_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_2'", 'null': 'True', 'to': "orm['flis.Indicator']"}),
            'indicator_3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_3'", 'null': 'True', 'to': "orm['flis.Indicator']"}),
            'indicator_4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_4'", 'null': 'True', 'to': "orm['flis.Indicator']"}),
            'trend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trend'", 'to': "orm['flis.Trend']"})
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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources_trend'", 'to': "orm['flis.Source']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['flis']