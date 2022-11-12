# This is where the URLs for our API are going to be stored
from django.urls import path

# Import our Views module which contains our API View
from profiles_api import views


# Just like our project's "url.py" file
# create list of path's that map to "views" in our project
# The URL that's going to map to our View is the webserver
# address/API/hello-view

urlpatterns = [path('hello-view/', views.HelloAPIView.as_view())]
