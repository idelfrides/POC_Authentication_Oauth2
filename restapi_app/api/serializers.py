""" Serializers module without a link group 
    that a user belongs 
""" 
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email', 
            "first_name", 
            "last_name", 
            'groups'
        )

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', "name")


