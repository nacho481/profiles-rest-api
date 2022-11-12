from django.shortcuts import render
# Imports the rest_framework
from rest_framework.views import APIView
# Imports the response Object which is used to return a response from the
# responses from the API View. A standard response object that when you call
# the API view or when the Django REST framework calls the API view
# it's expecting it to return the standard response object
from rest_framework.response import Response


# Creates a new class based on the Django APIView class
# Allows us to define the application logic for our "endpoint"
# In this case, the endpoint will be a URL, assign it to this view and the
# Django REST framework handles it by calling the appropriate function in the
# view for the HTTP request that you make.
class HelloAPIView(APIView):
    """Test API View"""

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

# Create your views here.
