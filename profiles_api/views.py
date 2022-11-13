from django.shortcuts import render
# Imports the rest_framework
from rest_framework.views import APIView
# Imports the response Object which is used to return a response from the
# responses from the API View. A standard response object that when you call
# the API view or when the Django REST framework calls the API view
# it's expecting it to return the standard response object
from rest_framework.response import Response
from rest_framework import viewsets
# List of handy HTTP status codes that you can use when returning responses
# from your API
from rest_framework import status
from profiles_api import serializers


# Creates a new class based on the Django APIView class
# Allows us to define the application logic for our "endpoint"
# In this case, the endpoint will be a URL, assign it to this view and the
# Django REST framework handles it by calling the appropriate function in the
# view for the HTTP request that you make.
class HelloAPIView(APIView):
    """Test API View"""
    # Configures the API View to have the serializer class that we created
    # in the previous video
    serializer_class = serializers.HelloSerializer
    # We'll be making an HTTP GET request
    def get(self, request, format=None):
        "Returns a list of API view features"
        # The way API Views are broken up is it expects a function with a
        # different HTTP request that can be made to the view so the HTTP GET
        # request is used to get a list of objects or a specific object
        # Essentially,
        # HTTP GET request -> HelloAPIView -> get(self, request, format=None)
        # The "self" parameter contains information on the view
        # The "request" is passed in by the Django REST framework and contains
        # details ont he request being made to the API
        # The "foramt" which is used to make a "format suffix" to the end of
        # the endpoint URL
        # it'   s best practice to keep the "format" parameter there

        # Define a list that defines all of the features of an API view
        # Essentially, returning an object in our API view
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over our application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message: ': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        # First retrieve the serializer then pass in the data that was
        # sent in the request
        # self.serializer_class() is a function that comes with the
        # API view retrieves the configured serializer class for our view
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # retrieves the name field
            name = serializer.validated_data.get('name')
            # using f string you can use the {} braces to insert a variable
            # into your string
            message = f'Hello {name}'
            return Response({'message': message})
            # return this if the request is not valid
        else:
            # provide errors, returns HTTP 200 request, change to 400 bad request
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    # used to update an object
    # done to a pk or primary key, we put it to none for now in case we don't
    # want to do that
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

# You add functions that represent actions on a typical API
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message' : 'hello', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new hello message"""
        # We pass the data from the request into the data variable which
        # we retrieved using the .serializer_class.
        serializer = self.serializer_class(data=request.data)

        # Validate it
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        # use with the PUT HTTP method
        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """Handle updating a part of an object"""
        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})
