# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RawProduct'
        db.create_table('product_rawproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('shelf_life', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('product', ['RawProduct'])

        # Adding model 'RegularUnit'
        db.create_table('product_regularunit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('std_qty', self.gf('django.db.models.fields.DecimalField')(default=1.0, max_digits=5, decimal_places=2)),
            ('std_unit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='standard_name', to=orm['product.RegularUnit'])),
        ))
        db.send_create_signal('product', ['RegularUnit'])

    def backwards(self, orm):
        # Deleting model 'RawProduct'
        db.delete_table('product_rawproduct')

        # Deleting model 'RegularUnit'
        db.delete_table('product_regularunit')

    models = {
        'product.rawproduct': {
            'Meta': {'object_name': 'RawProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shelf_life': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'product.regularunit': {
            'Meta': {'object_name': 'RegularUnit'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'std_qty': ('django.db.models.fields.DecimalField', [], {'default': '1.0', 'max_digits': '5', 'decimal_places': '2'}),
            'std_unit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'standard_name'", 'to': "orm['product.RegularUnit']"})
        }
    }

    complete_apps = ['product']