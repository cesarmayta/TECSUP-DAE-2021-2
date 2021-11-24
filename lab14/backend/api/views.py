from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import response
from rest_framework.permissions import isAuthenticated

@api_view(['GET'])
def publico(request):
    data = {
        'mensaje':'acceso publico'
    }
    return Response(data)
