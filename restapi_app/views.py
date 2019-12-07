""" views module """

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .managers.json_module import ManageAuthentication
from textwrap import dedent
import json, os


"""
--------------------------------------------
    views methods begin from here 
-------------------------------------------- 
"""
def resthome(request):
    pass
    data = {}
    data['wm'] = 'IDELFRIDES JORGE WM'
    data['title'] = 'Home | Django OAuth Toolkit '
    return render(request, 'resthome.html', data)


def get_token(request):
    maut = ManageAuthentication()
    os.chdir('restapi_app/managers')
    all_values = maut.solve_json_file('oauth_authorization.json')
    values_help = all_values.values()
    values_help = list(values_help)

    token = values_help[0]

    print(dedent(""" 

        THE TOKEN IS HERE -->  {}
    
        """.format(token))
    )
    
    data = {}
    data['wm'] = 'IDELFRIDES JORGE'
    data['title'] = 'Home | Django OAuth Toolkit'
    data['token'] = token
    return render(request, 'token.html', data)
    

'''
    36000s = 600m = 10h
'''