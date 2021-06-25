from django.http import response
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

import json

def get_csrf(request):
    response = JsonResponse({"info": "Success - Set CSRF cookie"})
    response['X-CSRFToken'] = get_token(request)
    return response


@require_POST
def loginView(request):
    data =  json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    if username is None or password is None:
        return JsonResponse({"info": "Username and Password is needed"})

    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({"info": "User does not exist"}, status=400)

    login(request, user)
    return JsonResponse({"info": "User logged in successfully"})
    