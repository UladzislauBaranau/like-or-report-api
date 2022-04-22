from rest_framework.permissions import BasePermission


class IsProfileOwner(BasePermission):
    """
    Allows access only to profile owner.

    Compares 'usernames' because they are unique.
    """

    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username
