from django.shortcuts import render
from rest_framework.decorators import api_view
from faculty.models import Faculty
from committee.models import Committee
import requests
from django.urls import reverse
from rest_framework.exceptions import AuthenticationFailed, NotFound
from django.conf import settings
from rest_framework.response import Response


@api_view(['POST'])
def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if email is None or password is None:
        raise AuthenticationFailed(detail="Fields are empty.", code=406)

    if Faculty.objects.filter(email=email).exists():
        data = {
            'email': email,
            'password': password,
            'access': settings.FACULTY_ACCESS
        }
        resp = requests.post(reverse('faculty:admin-login'), data=data)
        print(resp)
        return resp
    elif Committee.objects.filter(email=email).exists:
        data = {
            'email': email,
            'password': password,
            'access': settings.COMMITTEE_ACCESS
        }
        resp = requests.post(reverse('faculty:admin-login'), data=data)
        print(resp)
        return resp
    else:
        return Response({
            'details': 'chalega'
        })
