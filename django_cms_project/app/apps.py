from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'

    def ready( self ):
        from app import signals 
