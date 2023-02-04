from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed, NotFound
from .models import Faculty
from .serializers import AuthCommitteeSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    # print(username, password)

    user = Faculty.objects.filter(email=email).first()

    try:
        instance = user
        user = AuthCommitteeSerializer(user).data
    except Exception as e:
        return Response({
            'detail': "Error in serializing the data -> Specific error is " + str(e)
        }, status=500)

    # checking password
    if check_password(password, user.get('password')) == False:
        return Response({
            'detail': 'username or password is incorrect'
        }, status=401)

    # generating tokens
    try:
        access_token = instance.getAccessToken()
        refresh_token = instance.getRefreshToken()
        print('access_token => ', access_token)
        print('refresh_token => ', refresh_token)
    except Exception as e:
        return Response({
            'detail': "Error in generating tokens -> Specific error is " + str(e)
        }, status=500)

    response = Response({
        'user': user,
        'access_token': access_token,
        'access': request.POST.get('access'),
    })
    response.set_cookie('jwt_refresh_token', refresh_token, httponly=True)
    return response
