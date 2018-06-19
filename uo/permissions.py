from rest_framework import permissions


class UsersAccessPermission(permissions.BasePermission):
    """
    Allow new users to be created without authentication, all other requests
    must be by authenticated users.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated
