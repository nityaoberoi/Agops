# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RawProduct'
        db.delete_table('invoice_rawproduct')

        # Deleting model 'Vendor'
        db.delete_table('invoice_vendor')

        # Deleting model 'Country'
        db.delete_table('invoice_country')

        # Deleting model 'MenuItem'
        db.delete_table('invoice_menuitem')

        # Adding model 'InvoiceProduct'
        db.create_table('invoice_invoiceproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('raw_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.RawProduct'])),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoice.Brand'])),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.RegularUnit'])),
        ))
        db.send_create_signal('invoice', ['InvoiceProduct'])

        # Adding field 'Invoice.vendor'
        db.add_column('invoice_invoice', 'vendor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['vendor.Vendor']),
                      keep_default=False)

        # Deleting field 'InvoiceItem.product_number'
        db.delete_column('invoice_invoiceitem', 'product_number_id')

        # Adding field 'InvoiceItem.invoice'
        db.add_column('invoice_invoiceitem', 'invoice',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['invoice.Invoice']),
                      keep_default=False)

        # Adding field 'InvoiceItem.invoice_product'
        db.add_column('invoice_invoiceitem', 'invoice_product',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['invoice.InvoiceProduct']),
                      keep_default=False)

    def backwards(self, orm):
        # Adding model 'RawProduct'
        db.create_table('invoice_rawproduct', (
            ('vendor_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoice.Brand'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('shelf_life', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('invoice', ['RawProduct'])

        # Adding model 'Vendor'
        db.create_table('invoice_vendor', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoice.Country'], null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(unique=True, max_length=20, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('invoice', ['Vendor'])

        # Adding model 'Country'
        db.create_table('invoice_country', (
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150, unique=True)),
        ))
        db.send_create_signal('invoice', ['Country'])

        # Adding model 'MenuItem'
        db.create_table('invoice_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shelf_life', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('invoice', ['MenuItem'])

        # Deleting model 'InvoiceProduct'
        db.delete_table('invoice_invoiceproduct')

        # Deleting field 'Invoice.vendor'
        db.delete_column('invoice_invoice', 'vendor_id')

        # Adding field 'InvoiceItem.product_number'
        db.add_column('invoice_invoiceitem', 'product_number',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['invoice.RawProduct']),
                      keep_default=False)

        # Deleting field 'InvoiceItem.invoice'
        db.delete_column('invoice_invoiceitem', 'invoice_id')

        # Deleting field 'InvoiceItem.invoice_product'
        db.delete_column('invoice_invoiceitem', 'invoice_product_id')

    models = {
        'invoice.brand': {
            'Meta': {'object_name': 'Brand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'invoice.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vendor.Vendor']"})
        },
        'invoice.invoiceitem': {
            'Meta': {'object_name': 'InvoiceItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoice.Invoice']"}),
            'invoice_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoice.InvoiceProduct']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'invoice.invoiceproduct': {
            'Meta': {'object_name': 'InvoiceProduct'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoice.Brand']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'raw_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.RawProduct']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.RegularUnit']"})
        },
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
        'vendor.country': {
            'Meta': {'object_name': 'Country'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'vendor.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vendor.Country']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['invoice']