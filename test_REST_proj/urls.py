"""test_REST_proj URL Configuration

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
-----------------------------------------------------

 --> this urls sonfiguration is only about  django REST framework

"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User, Group
from restapi_app import views 
from rest_framework import routers 
from restapi_app.views import resthome
from restapi_app.api.viewsets import UserViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-rest/', include(router.urls)),
    path(
        'api-auth/', include(
                    'rest_framework.urls', 
                    namespace='rest_framework'
                )
    ),
    path('', resthome, name='url_home'),
]


