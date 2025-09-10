from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException

@api_view(["GET"])
def health_check(request):
    """Vue DRF simple qui renvoie un JSON de santé."""
    return Response({"status": "ok", "message": "API is healthy"})  # 200 par défaut

@api_view(["GET"])
def trigger_error(request):
    """Deux variantes au choix pour provoquer une erreur 500 :"""

    # Variante A — vrai 500 non intercepté (traceback) :
    # 1 / 0  # décommente pour tester un vrai crash 500

    # Variante B — 500 “propre” au format DRF JSON :
    raise APIException("Erreur volontaire (test 500)")  # retourne 500 JSON DRF
    # ou: return Response({"detail": "Erreur volontaire"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
