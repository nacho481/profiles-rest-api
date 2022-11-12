from rest_framework import serializers


# Base it on the serializer class from the Django Rest framework
# 2nd is a class name so its got a capital S
class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    # Create a serializer that accepts a name input and add to our API View
    # use it to test the POST functionality of our API View

    # Creates a new name field
    name = serializers.CharField(max_length=10)
