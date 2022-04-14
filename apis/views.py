from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings

from apis import models
from apis import permissions
from apis import serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'phone',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ContentViewSet(viewsets.ModelViewSet):
    """Handles create view and update content items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ContentSerializer
    queryset = models.Content.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'body', 'summary', 'categories')
    permission_classes = (
        permissions.IsOwnContent,
        permissions.IsAdmin,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged-in User"""
        serializer.save(user_profile=self.request.user)
