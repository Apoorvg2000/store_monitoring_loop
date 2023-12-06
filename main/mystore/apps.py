"""
This module defines the configuration for the "mystore" Django application.
It includes settings specific to this application such as its name and default auto field type.
"""
from django.apps import AppConfig


# MystoreConfig class defines the application configuration for the 'mystore' app.
class MystoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mystore'
