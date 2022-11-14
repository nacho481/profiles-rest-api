# This is where the URLs for our API are going to be stored
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Import our Views module which contains our API View
from profiles_api import views


# Just like our project's "url.py" file
# create list of path's that map to "views" in our project
# The URL that's going to map to our View is the webserver
# address/API/hello-view

router = DefaultRouter()

# Create url within the ()
# router creates a url for us so we don't need to include the '/'
# 2nd arg is the ViewSet we wish to register
# this is used to retrieve URLs from our router
router.register('hello-ViewSet', views.HelloViewSet, base_name='hello-viewset')

# Register model viewset
# we don't need to specify a base_name object b/c we declared a query set object
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]

# To provide a ViewSet you have to use a "router" which is a class provided
# by the Django REST framework in order to generate the different routes
# that are available for our viewset

# path('', include(router.urls)) helps generate a list of urls that are
# associated with our ViewSet
# we have an empty string because we don't want to include a prefix
