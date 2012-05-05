# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Invoice'
        db.create_table('invoice_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('invoice', ['Invoice'])

        # Adding model 'InvoiceItem'
        db.create_table('invoice_invoiceitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoice.RawProduct'])),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('invoice', ['InvoiceItem'])

        # Adding model 'RawProduct'
        db.create_table('invoice_rawproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vendor_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoice.Brand'])),
            ('shelf_life', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('invoice', ['RawProduct'])

        # Adding model 'Brand'
        db.create_table('invoice_brand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('invoice', ['Brand'])

        # Adding model 'Vendor'
        db.create_table('invoice_vendor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoice.Country'], null=True)),
            ('phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('invoice', ['Vendor'])

        # Adding model 'MenuItem'
        db.create_table('invoice_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('shelf_life', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('invoice', ['MenuItem'])

        # Adding model 'Country'
        db.create_table('invoice_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('invoice', ['Country'])

    def backwards(self, orm):
        # Deleting model 'Invoice'
        db.delete_table('invoice_invoice')

        # Deleting model 'InvoiceItem'
        db.delete_table('invoice_invoiceitem')

        # Deleting model 'RawProduct'
        db.delete_table('invoice_rawproduct')

        # Deleting model 'Brand'
        db.delete_table('invoice_brand')

        # Deleting model 'Vendor'
        db.delete_table('invoice_vendor')

        # Deleting model 'MenuItem'
        db.delete_table('invoice_menuitem')

        # Deleting model 'Country'
        db.delete_table('invoice_country')

    models = {
        'invoice.brand': {
            'Meta': {'object_name': 'Brand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'invoice.country': {
            'Meta': {'object_name': 'Country'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'invoice.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'invoice.invoiceitem': {
            'Meta': {'object_name': 'InvoiceItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'product_number': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoice.RawProduct']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'invoice.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shelf_life': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'invoice.rawproduct': {
            'Meta': {'object_name': 'RawProduct'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoice.Brand']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shelf_life': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'vendor_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'invoice.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoice.Country']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['invoice']