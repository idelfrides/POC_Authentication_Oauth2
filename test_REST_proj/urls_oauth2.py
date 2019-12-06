""" This is the urls file for django Oauth Toolkit """

from django.urls import path, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
from restapi_app.views import get_token, resthome
from restapi_app.api.api_views import UserList, UserDetails, GroupList
from rest_framework import routers
from restapi_app.api.viewsets import UserViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)


''' Setup the URLs and include login URLs
    for the browsable API.
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', resthome, name='url_resthome'),
    path(
        'o/', 
        include(
            'oauth2_provider.urls', 
            namespace='oauth2_provider'
        )
    ),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    # path('token/', get_token, name='url_token'),

    path('api-rest/', include(router.urls)),
    path(
        'api-auth/', 
        include(
            'rest_framework.urls', 
            namespace='rest_framework'
        )
    ),
    
]
