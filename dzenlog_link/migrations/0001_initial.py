from django.utils.translation import ugettext_lazy as _
from south.db import db
from django.db import models
from dzenlog_link.models import *

class Migration:
    
    def forwards(self):
        
        
        # Mock Models
        GeneralPost = db.mock_model(model_name='GeneralPost', db_table='django_dzenlog_generalpost', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[])
        
        # Model 'LinkPost'
        db.create_table('dzenlog_link_linkpost', (
            ('generalpost_ptr', models.OneToOneField(GeneralPost)),
            ('url', models.URLField(_('URL'), verify_exists = not settings.DEBUG)),
            ('description', models.TextField(_('URL\'s description'), max_length = 255)),
        ))
        
        db.send_create_signal('dzenlog_link', ['LinkPost'])
    
    def backwards(self):
        db.delete_table('dzenlog_link_linkpost')
        
