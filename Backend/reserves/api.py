from rest_framework import viewsets, permissions
from .models import Reserve
from .serializers import ReserveSerializer

class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReserveSerializer