"""
Creates the default Site object.
"""

from django.apps import apps as global_apps
from django.conf import settings
from django.core.management.color import no_style
from django.db import DEFAULT_DB_ALIAS, connections, router


def create_default_site(app_config, verbosity=2, interactive=True, using=DEFAULT_DB_ALIAS, apps=global_apps, **kwargs):
    try:
        Site = apps.get_model('src.frontend', 'Pages')
    except LookupError:
        return

    if not router.allow_migrate_model(using, Site):
        return

    if not Site.objects.using(using).exists():
        # The default settings set SITE_ID = 1, and some tests in Django's test
        # suite rely on this value. However, if database sequences are reused
        # (e.g. in the test suite after flush/syncdb), it isn't guaranteed that
        # the next id will be 1, so we coerce it. See #15573 and #16353. This
        # can also crop up outside of tests - see #15346.
        if verbosity >= 2:
            print("Creating Pages")
        Site(
            en_name="Home",
            es_name="Inicio",
            en_desc="Home Page",
            es_desc="Página de Inicio",
            en_title="Home Page",
            es_title="Página de Inicio",
            en_url="es:es",
            es_url="en:en",
        ).save(using=using)

        # We set an explicit pk instead of relying on auto-incrementation,
        # so we need to reset the database sequence. See #17415.
        # sequence_sql = connections[using].ops.sequence_reset_sql(no_style(), [Site])
        # if sequence_sql:
        #     if verbosity >= 2:
        #         print("Resetting sequence")
        #     with connections[using].cursor() as cursor:
        #         for command in sequence_sql:
        #             cursor.execute(command)