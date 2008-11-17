from django.contrib import admin
from models import LinkPost
from django_dzenlog.admin import GeneralPostAdmin

admin.site.register(LinkPost, GeneralPostAdmin)
