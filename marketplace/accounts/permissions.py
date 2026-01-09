from rest_framework import permissions

class IsBusinessAdmin(permissions.BasePermission):
    """
    Only allow users with can_manage_users=True to manage users
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role and request.user.role.can_manage_users
