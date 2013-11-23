# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('flis_country', (
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=128, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('flis', ['Country'])

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
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trends', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['Trend'])

        # Adding model 'Blossom'
        db.create_table('flis_blossom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=56, null=True)),
            ('title_original', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('new_or_update', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('ownership', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=56, null=True)),
            ('who_is_doing', self.gf('django.db.models.fields.CharField')(max_length=56, null=True)),
            ('purpose_and_target_audience', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('stakeholders_study_planned', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('stakeholders_study_final', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('stakeholders_review_planned', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('stakeholders_review_final', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('time_plan_planned', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('time_plan_final', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('date_of_conclusion_planned', self.gf('django.db.models.fields.DateField')(null=True)),
            ('date_of_conclusion_final', self.gf('django.db.models.fields.DateField')(null=True)),
            ('project_team', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('stakeholders', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('other_parties', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('networks', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=512, blank=True)),
        ))
        db.send_create_signal('flis', ['Blossom'])

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

        # Adding model 'Scenario'
        db.create_table('flis_scenario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('flis', ['Scenario'])

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
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('thematic_category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Indicators', on_delete=models.PROTECT, to=orm['flis.ThematicCategory'])),
            ('geographical_scale', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Indicators', null=True, on_delete=models.PROTECT, to=orm['flis.GeographicalScale'])),
            ('geographical_coverage', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Indicators', null=True, on_delete=models.PROTECT, to=orm['flis.GeographicalCoverage'])),
            ('timeline', self.gf('django.db.models.fields.related.ForeignKey')(related_name='timeline', on_delete=models.PROTECT, to=orm['flis.Timeline'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sources_indicator', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('base_year', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('end_year', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['Indicator'])

        # Adding model 'GMT'
        db.create_table('flis_gmt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('steep_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gmts', null=True, on_delete=models.PROTECT, to=orm['flis.SteepCategory'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gmts', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['GMT'])

        # Adding model 'FlisModel'
        db.create_table('flis_flismodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('steep_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='flismodels', null=True, on_delete=models.PROTECT, to=orm['flis.SteepCategory'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flismodels', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['FlisModel'])

        # Adding model 'HorizonScanning'
        db.create_table('flis_horizonscanning', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('steep_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='horizonscannings', null=True, on_delete=models.PROTECT, to=orm['flis.SteepCategory'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='horizonscannings', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['HorizonScanning'])

        # Adding model 'MethodTool'
        db.create_table('flis_methodtool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('steep_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='methodstools', null=True, on_delete=models.PROTECT, to=orm['flis.SteepCategory'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='methodstools', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['MethodTool'])

        # Adding model 'Uncertainty'
        db.create_table('flis_uncertainty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('steep_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='uncertainties', null=True, on_delete=models.PROTECT, to=orm['flis.SteepCategory'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='uncertainties', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['Uncertainty'])

        # Adding model 'WildCard'
        db.create_table('flis_wildcard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('steep_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='wildcards', null=True, on_delete=models.PROTECT, to=orm['flis.SteepCategory'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wildcards', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['WildCard'])

        # Adding model 'EarlyWarning'
        db.create_table('flis_earlywarning', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('steep_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='earlywarnings', null=True, on_delete=models.PROTECT, to=orm['flis.SteepCategory'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='earlywarnings', on_delete=models.PROTECT, to=orm['flis.Source'])),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.files.FileField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('flis', ['EarlyWarning'])

        # Adding model 'Interlink'
        db.create_table('flis_interlink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flis.Country'])),
            ('gmt', self.gf('django.db.models.fields.related.ForeignKey')(related_name='interlinks', to=orm['flis.GMT'])),
            ('trend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='interlinks', on_delete=models.PROTECT, to=orm['flis.Trend'])),
            ('indicator_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='interlinks_indicator_1', on_delete=models.PROTECT, to=orm['flis.Indicator'])),
            ('indicator_2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='interlinks_indicator_2', null=True, on_delete=models.PROTECT, to=orm['flis.Indicator'])),
            ('indicator_3', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='interlinks_indicator_3', null=True, on_delete=models.PROTECT, to=orm['flis.Indicator'])),
            ('indicator_4', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='interlinks_indicator_4', null=True, on_delete=models.PROTECT, to=orm['flis.Indicator'])),
        ))
        db.send_create_signal('flis', ['Interlink'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('flis_country')

        # Deleting model 'Source'
        db.delete_table('flis_source')

        # Deleting model 'Trend'
        db.delete_table('flis_trend')

        # Deleting model 'Blossom'
        db.delete_table('flis_blossom')

        # Deleting model 'ThematicCategory'
        db.delete_table('flis_thematiccategory')

        # Deleting model 'GeographicalScale'
        db.delete_table('flis_geographicalscale')

        # Deleting model 'GeographicalCoverage'
        db.delete_table('flis_geographicalcoverage')

        # Deleting model 'Scenario'
        db.delete_table('flis_scenario')

        # Deleting model 'SteepCategory'
        db.delete_table('flis_steepcategory')

        # Deleting model 'Timeline'
        db.delete_table('flis_timeline')

        # Deleting model 'Indicator'
        db.delete_table('flis_indicator')

        # Deleting model 'GMT'
        db.delete_table('flis_gmt')

        # Deleting model 'FlisModel'
        db.delete_table('flis_flismodel')

        # Deleting model 'HorizonScanning'
        db.delete_table('flis_horizonscanning')

        # Deleting model 'MethodTool'
        db.delete_table('flis_methodtool')

        # Deleting model 'Uncertainty'
        db.delete_table('flis_uncertainty')

        # Deleting model 'WildCard'
        db.delete_table('flis_wildcard')

        # Deleting model 'EarlyWarning'
        db.delete_table('flis_earlywarning')

        # Deleting model 'Interlink'
        db.delete_table('flis_interlink')


    models = {
        'flis.blossom': {
            'Meta': {'object_name': 'Blossom'},
            'date_of_conclusion_final': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_of_conclusion_planned': ('django.db.models.fields.DateField', [], {'null': 'True'}),
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'title_original': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trends'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.uncertainty': {
            'Meta': {'object_name': 'Uncertainty'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
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