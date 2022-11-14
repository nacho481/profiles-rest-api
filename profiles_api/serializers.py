from rest_framework import serializers
from profiles_api import models

# Base it on the serializer class from the Django Rest framework
# 2nd is a class name so its got a capital S
class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    # Create a serializer that accepts a name input and add to our API View
    # use it to test the POST functionality of our API View

    # Creates a new name field
    name = serializers.CharField(max_length=10)

# We're going to be adding a model serializer, except it has more functionality
# than a normal serializer which makes it easier to work with existing
# Django database models
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""
    # You define a serializer by defining a metha class
    class Meta:
        # sets our serializer up to point to our user model
        # use a tuple
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True, # password field set to true, only write to
                'style' : {'input_type' : 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        # create and return a new user from our model manager
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    # Issue
    # If a user updates their profile, the password field is stored in
    # cleartext, and they are unable to login.

    # Cause
    # Override Django REST Frameworks ModelSerializer to hash the users
    # password when updating

    # Explanation
    # Default update logic for Django Rest Framework (DRF)
    # takes whatever fields are provided and pass them directly to the model
    #
    # It's fine except for password b/c it requires additional logic to be
    # hashed before saving the update
    #
    # Thus, we override the update() function to add this logic
    #
    # if the field exists, pop the value and set the password using
    # the set_password() function to set the hash
    #
    # once that's done, use super.update() to pass the values of the existing
    # DRF update() method, to handle updating the remaining fields
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
