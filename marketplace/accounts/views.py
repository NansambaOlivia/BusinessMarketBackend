from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Role
from .serializers import UserSerializer, RoleSerializer
from .permissions import IsBusinessAdmin

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsBusinessAdmin]

    def get_queryset(self):
        # Handle schema generation for Swagger
        if getattr(self, 'swagger_fake_view', False):
            return User.objects.none()
            
        # Users from the same business only
        return User.objects.filter(business=self.request.user.business)

    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, IsBusinessAdmin]

