from django.urls import path
from .views import health_check, trigger_error

urlpatterns = [
    path("health/", health_check, name="health_check"),
    path("trigger-error/", trigger_error, name="trigger_error"),
]
