from __future__ import unicode_literals

from django.apps import AppConfig
from django.db import migrations
from django.utils.translation import ugettext_lazy as _

class BrandsConfig(AppConfig):
    name = 'src.brands'
    verbose_name = _("Módulo marcas")


