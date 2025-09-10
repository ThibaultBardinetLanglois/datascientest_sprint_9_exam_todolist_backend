from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException

@api_view(["GET"])
def health_check(request):
    """Vue DRF simple qui renvoie un JSON de santé."""
    return Response({"status": "ok", "message": "API is healthy"})  # 200 par défaut

@api_view(["GET"])
def trigger_error(request):
    """Vue DRF simple qui renvoie un 500 :"""
    1 / 0  
    return Response({"this": "will never be returned"})
