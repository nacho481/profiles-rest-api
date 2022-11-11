from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# PEP-8 Guidelines say that classes in a Python module should be two spaces
# between them
from django.contrib.auth.models import BaseUserManager


# Create your models here.
# Inherit from base user manager which is the DEFAULT user manager that comes
# with Django
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    # Managers: you specify some functions within the manager that can be used
    # to manipulate objects within

    def create_user(self, email, name, password=None):
        # If the empty is an "empty string" or a "null" value
        # Raise an exception and catch an error
        if not email:
            raise ValueError('Users must have an email address')

        # Normalize your email address by making the 2nd half lowercase
        # 1st half, case-sensitive, 2nd half case-insensitive
        # 1st half by Gmail and Hotmaill are all lower case by default for
        # convience, but just know it is possible it's case-sensitive
        email = self.normalize_email(email)

        # Creates a new model that the user manager is representing
        # New model object setting the email and the name
        user = self.model(email=email, name=name)

        # Set the password using the .set_password() function that comes with
        # the AbstractBaseUser class
        # Encrypts password, converted to hash so hackers can only see
        # a hashed password. Best practice but they can still reverse engineer
        # it
        user.set_password(password)

        # Save profile, add to add database
        # Standard procedure for saving objects in Django
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details"""
        # self is ALWAYS passed into the function
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin ):
    """Database models for users in the system"""
    # Create an email column in the db table
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    # By default, we'll set the user's profile as active
    # we can deactivate users at some point in the future if needed
    is_active = models.BooleanField(default=True)

    # Determine if user is a staff user with admin perms, set to false
    is_staff = models.BooleanField(default=False)

    # Django CLI Django needs to have a custom model manager for the user
    # model to know how to create and control users using Django
    # command line tools

    # Create a UserProfileManager
    objects = UserProfileManager()

    # Overriding default username, replacing with email field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # because we're defining a function in a class we must specify "self"
    # as the first argument, default Python convention
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    # Represent a string representation of our model now
    # when we want to convert a "user profile object" into a "string" in Python
    # recommended for all Django models!
    def __str__(self):
        """Return string representation of our user"""
        return self.email
