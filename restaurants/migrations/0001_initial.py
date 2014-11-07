# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table(u'restaurants_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('google_rating', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('up_vote', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('down_vote', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('price_level', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'restaurants', ['Restaurant'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table(u'restaurants_restaurant')


    models = {
        u'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'down_vote': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'google_rating': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price_level': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'up_vote': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['restaurants']