from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if logged-in user and the accessed profile id is same
        if request.user.id == obj.id:
            return True


class IsOwnContent(permissions.BasePermission):
    """Allow users to view, edit, delete only their own content"""

    def has_object_permission(self, request, view, obj):
        """Check user has access to their own content"""
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if logged-in user is the owner of the content
        if request.user.id == obj.user_profile.id:
            return True


class IsAdmin(permissions.BasePermission):
    """Allow Admin users to edit, delete anyone's content"""

    def has_object_permission(self, request, view, obj):
        """Check if logged-in user is Admin"""
        return request.user.is_staff
