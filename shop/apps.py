from django.apps import AppConfig

class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

    def ready(self):
        import shop.signals  # подключаем сигналы при запуске приложения

from django.apps import AppConfig

class ShopConfig(AppConfig):
    name = 'shop'

    def ready(self):
        import shop.signals  # Убедитесь, что сигнал будет загружен
