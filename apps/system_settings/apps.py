from django.apps import AppConfig


class SystemSettingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.system_settings"

    def ready(self):
        """Import signals when Django is ready"""
        import apps.system_settings.signals  # noqa
