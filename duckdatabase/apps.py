from django.apps import AppConfig

# only one application, the main duck database
class DuckdatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'duckdatabase'
