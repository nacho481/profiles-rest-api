from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    # use has object perm to class which is called every time a function
    # call to the API is made, returns T/F

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # check if the object they're updating matches their authenticated
        # user profile that matches to the authentication of the request
        # when authenticated it will assign the (auth user) to the
        # (auth request)
        if request.method in permissions.SAFE_METHOD:
            return True

        # if this is true, the it will evaluate to true.
        return obj.id == request.user.id
