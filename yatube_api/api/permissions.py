from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Кастомной пермишн, который разрешает полный доступ к объекту только автору
    """
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
