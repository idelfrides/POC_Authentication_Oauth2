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
    data['title'] = 'Home | Django REST '
    return render(request, 'resthome.html', data)


def get_token(request):
    maut = ManageAuthentication()
    # ------------------------------
    #            WAY 1
    # ------------------------------
    # current_dir = os.getcwd()
    # os.chdir(current_dir + '/managers/')
    # all_values = maut.solve_json_file('oauth_authorization.json')

    # ------------------------------
    #            WAY 2
    # ------------------------------
    current_dir = os.getcwd() + '/managers/' 
    thepath = current_dir + 'oauth_authorization.json'
    
    all_values = maut.solve_json_file(thepath)
    values_help = all_values.values()
    values_help = list(values_help)

    token = values_help[0]  

    print(dedent(""" 

        THE TOKEN IS HERE -->  {}
    
        """.format(token))
    )
    
    data = {}
    data['wm'] = 'IDELFRIDES JORGE'
    data['title'] = 'Home | Django REST OAUTH2 '
    data['token'] = token
    return render(request, 'token.html', data)
    



