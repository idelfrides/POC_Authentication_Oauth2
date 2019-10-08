from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .managers.json_module import solve_json_file
import json, os

"""
--------------------------------------------
     views methods begin from here 
 ------------------------------------------- 
"""
def resthome(request):
    pass
    data = {}
    data['wm'] = 'IDELFRIDES JORGE WM'
    data['title'] = 'Home | Django REST '
    return render(request, 'resthome.html', data)


def get_token(request):

    os.chdir('restapi_app/managers')  # change to app directory
    all_values = solve_json_file()      # a dict
    values_help = all_values.values()   # get just a dict of values
    values_help = list(values_help)     

    token = values_help[0]  

    print('\n\n THE TOKEN IS HERE -->  {}'.format(token))
    print('\n\n\n')

    data = {}
    data['wm'] = 'IDELFRIDES JORGE WM'
    data['title'] = 'Home | Django REST '
    data['token'] = token
    return render(request, 'token.html', data)


