""" API views module """

from django.contrib import admin
from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions

from .serializers import UserSerializer, GroupSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from oauth2_provider.contrib.rest_framework import TokenHasScope

admin.autodiscover()


# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated, 
        TokenHasReadWriteScope
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated, 
        TokenHasReadWriteScope
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class GroupList(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated, 
        TokenHasScope
    ]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

