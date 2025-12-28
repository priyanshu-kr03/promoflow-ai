from .models import Organization
from rest_framework.exceptions import AuthenticationFailed

def authenticate_org(request):
    api_key = request.headers.get("X-API-KEY")

    if not api_key:
        raise AuthenticationFailed("API key missing")

    try:
        return Organization.objects.get(api_key=api_key)
    except Organization.DoesNotExist:
        raise AuthenticationFailed("Invalid API key")
