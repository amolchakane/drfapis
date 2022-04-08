from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from apis import serializers
from apis import models
from apis import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'phone',)
