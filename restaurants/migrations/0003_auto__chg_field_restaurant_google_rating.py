# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Restaurant.google_rating'
        db.alter_column(u'restaurants_restaurant', 'google_rating', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

    def backwards(self, orm):

        # Changing field 'Restaurant.google_rating'
        db.alter_column(u'restaurants_restaurant', 'google_rating', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

    models = {
        u'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'down_vote': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'google_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'icon': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price_level': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'up_vote': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['restaurants']