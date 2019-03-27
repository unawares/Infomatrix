from rest_framework import permissions

class IsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return user.has_perm('users.manager')
        return False