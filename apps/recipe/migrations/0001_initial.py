# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table('recipe_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('shelf_life', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('recipe', ['Recipe'])

        # Adding model 'RecipeItem'
        db.create_table('recipe_recipeitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipe.Recipe'])),
            ('raw_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.RawProduct'])),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.RegularUnit'])),
        ))
        db.send_create_signal('recipe', ['RecipeItem'])

    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table('recipe_recipe')

        # Deleting model 'RecipeItem'
        db.delete_table('recipe_recipeitem')

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
        },
        'recipe.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'shelf_life': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'recipe.recipeitem': {
            'Meta': {'object_name': 'RecipeItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'raw_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.RawProduct']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipe.Recipe']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.RegularUnit']"})
        }
    }

    complete_apps = ['recipe']