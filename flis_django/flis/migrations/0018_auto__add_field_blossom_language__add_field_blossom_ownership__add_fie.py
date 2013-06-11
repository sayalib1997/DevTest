# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blossom.language'
        db.add_column('flis_blossom', 'language',
                      self.gf('django.db.models.fields.CharField')(max_length=56, null=True),
                      keep_default=False)

        # Adding field 'Blossom.ownership'
        db.add_column('flis_blossom', 'ownership',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.status'
        db.add_column('flis_blossom', 'status',
                      self.gf('django.db.models.fields.CharField')(max_length=56, null=True),
                      keep_default=False)

        # Adding field 'Blossom.who_is_doing'
        db.add_column('flis_blossom', 'who_is_doing',
                      self.gf('django.db.models.fields.CharField')(max_length=56, null=True),
                      keep_default=False)

        # Adding field 'Blossom.purpose_and_target_audience'
        db.add_column('flis_blossom', 'purpose_and_target_audience',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.stakeholders_study_planned'
        db.add_column('flis_blossom', 'stakeholders_study_planned',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.stakeholders_study_final'
        db.add_column('flis_blossom', 'stakeholders_study_final',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.stakeholders_review_planned'
        db.add_column('flis_blossom', 'stakeholders_review_planned',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.stakeholders_review_final'
        db.add_column('flis_blossom', 'stakeholders_review_final',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.time_plan_planned'
        db.add_column('flis_blossom', 'time_plan_planned',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.time_plan_final'
        db.add_column('flis_blossom', 'time_plan_final',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.date_of_conclusion_planned'
        db.add_column('flis_blossom', 'date_of_conclusion_planned',
                      self.gf('django.db.models.fields.CharField')(max_length=56, null=True),
                      keep_default=False)

        # Adding field 'Blossom.date_of_conclusion_final'
        db.add_column('flis_blossom', 'date_of_conclusion_final',
                      self.gf('django.db.models.fields.CharField')(max_length=56, null=True),
                      keep_default=False)

        # Adding field 'Blossom.project_team'
        db.add_column('flis_blossom', 'project_team',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.stakeholders'
        db.add_column('flis_blossom', 'stakeholders',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.other_parties'
        db.add_column('flis_blossom', 'other_parties',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blossom.networks'
        db.add_column('flis_blossom', 'networks',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blossom.language'
        db.delete_column('flis_blossom', 'language')

        # Deleting field 'Blossom.ownership'
        db.delete_column('flis_blossom', 'ownership')

        # Deleting field 'Blossom.status'
        db.delete_column('flis_blossom', 'status')

        # Deleting field 'Blossom.who_is_doing'
        db.delete_column('flis_blossom', 'who_is_doing')

        # Deleting field 'Blossom.purpose_and_target_audience'
        db.delete_column('flis_blossom', 'purpose_and_target_audience')

        # Deleting field 'Blossom.stakeholders_study_planned'
        db.delete_column('flis_blossom', 'stakeholders_study_planned')

        # Deleting field 'Blossom.stakeholders_study_final'
        db.delete_column('flis_blossom', 'stakeholders_study_final')

        # Deleting field 'Blossom.stakeholders_review_planned'
        db.delete_column('flis_blossom', 'stakeholders_review_planned')

        # Deleting field 'Blossom.stakeholders_review_final'
        db.delete_column('flis_blossom', 'stakeholders_review_final')

        # Deleting field 'Blossom.time_plan_planned'
        db.delete_column('flis_blossom', 'time_plan_planned')

        # Deleting field 'Blossom.time_plan_final'
        db.delete_column('flis_blossom', 'time_plan_final')

        # Deleting field 'Blossom.date_of_conclusion_planned'
        db.delete_column('flis_blossom', 'date_of_conclusion_planned')

        # Deleting field 'Blossom.date_of_conclusion_final'
        db.delete_column('flis_blossom', 'date_of_conclusion_final')

        # Deleting field 'Blossom.project_team'
        db.delete_column('flis_blossom', 'project_team')

        # Deleting field 'Blossom.stakeholders'
        db.delete_column('flis_blossom', 'stakeholders')

        # Deleting field 'Blossom.other_parties'
        db.delete_column('flis_blossom', 'other_parties')

        # Deleting field 'Blossom.networks'
        db.delete_column('flis_blossom', 'networks')


    models = {
        'flis.blossom': {
            'Meta': {'object_name': 'Blossom'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'date_of_conclusion_final': ('django.db.models.fields.CharField', [], {'max_length': '56', 'null': 'True'}),
            'date_of_conclusion_planned': ('django.db.models.fields.CharField', [], {'max_length': '56', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '56', 'null': 'True'}),
            'networks': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'new_or_update': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'other_parties': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ownership': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'project_team': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'purpose_and_target_audience': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders_review_final': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders_review_planned': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders_study_final': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders_study_planned': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '56', 'null': 'True'}),
            'time_plan_final': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'time_plan_planned': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'who_is_doing': ('django.db.models.fields.CharField', [], {'max_length': '56', 'null': 'True'})
        },
        'flis.country': {
            'Meta': {'object_name': 'Country'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'flis.earlywarning': {
            'Meta': {'object_name': 'EarlyWarning'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'earlywarnings'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'earlywarnings'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.flismodel': {
            'Meta': {'object_name': 'FlisModel'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flismodels'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'flismodels'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
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
        'flis.horizonscanning': {
            'Meta': {'object_name': 'HorizonScanning'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'horizonscannings'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'horizonscannings'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
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
        'flis.methodtool': {
            'Meta': {'object_name': 'MethodTool'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'methodstools'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'methodstools'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        },
        'flis.uncertainty': {
            'Meta': {'object_name': 'Uncertainty'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uncertainties'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'uncertainties'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.wildcard': {
            'Meta': {'object_name': 'WildCard'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wildcards'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'wildcards'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['flis']