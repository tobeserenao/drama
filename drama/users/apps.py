from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "drama.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import drama.users.signals  # noqa: F401
        except ImportError:
            pass
