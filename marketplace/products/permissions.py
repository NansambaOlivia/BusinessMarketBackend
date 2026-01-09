from rest_framework import permissions

class CanApproveProduct(permissions.BasePermission):
    """
    Only users with `can_approve_products` role permission can approve products.
    """

    def has_permission(self, request, view):
        return True  # allow general access; object-level handles approval

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'PUT'] and 'status' in request.data:
            # Only allow status changes to approved if user can approve
            if request.data['status'] == 'approved':
                return getattr(request.user.role, 'can_approve_products', False)
        return True
