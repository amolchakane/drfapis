from rest_framework import serializers

from apis import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'phone', 'address', 'city', 'state', 'country', 'pincode')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
            pincode=validated_data['pincode']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


# We will be creating serializer for Content model
class ContentSerializer(serializers.ModelSerializer):
    """Serializes content object"""

    class Meta:
        model = models.Content
        fields = ('id', 'user_profile', 'title', 'body', 'summary', 'document', 'categories', 'created_on')
        # User profile can only be read only
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
