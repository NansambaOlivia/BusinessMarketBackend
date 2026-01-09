from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer
from .permissions import CanApproveProduct

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, CanApproveProduct]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Product.objects.filter(business=user.business)

        return Product.objects.filter(status='approved')

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            business=self.request.user.business
        )
