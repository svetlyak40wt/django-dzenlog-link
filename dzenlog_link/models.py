from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_dzenlog.models import GeneralPost
from django.conf import settings

class LinkPost(GeneralPost):
    list_template             = 'dzenlog_link/list.html'
    detail_template           = 'dzenlog_link/detail.html'
    body_detail_template      = 'dzenlog_link/body_detail.html'
    body_list_template        = 'dzenlog_link/body_list.html'
    feed_description_template = 'dzenlog_link/text_feed_detail.html'

    url = models.URLField(_('URL'), verify_exists = not settings.DEBUG)
    description = models.TextField(_('URL\'s description'), max_length = 255)

    class Meta:
        verbose_name = _('link post')
        verbose_name_plural = _('link posts')
