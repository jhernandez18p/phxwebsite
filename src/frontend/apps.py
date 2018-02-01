from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _



class FrontendConfig(AppConfig):
    name = 'src.frontend'
    verbose_name = _('Detalles de la página web')
