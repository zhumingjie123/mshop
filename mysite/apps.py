from django.apps import AppConfig

class PaymentConfig(AppConfig):
    name = 'mysite'
    verbose_name = 'Mysite'

    def ready(self):
        import mysite.signal
