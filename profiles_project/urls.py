"""profiles_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from profiles_api import views
# "include" is a function that you can use to include URLs from other apps
# in the root project URLs file

# check for matching base URL API then anything after the / will pass
# through and match the to the "api/urls.py"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]

# when you go /api in the webserver, it will pass in the request in our
# Django app which will look at the "urlpatterns" which matches the URL
# that we've entered.
# Then it will pass in all of the URLs that match with the API URLs
#   path('api', include("profiles_api.urls"))
# then it will load all sub URLs (the project_api.url file) in our urls.py
# the one in (profiles_project)
