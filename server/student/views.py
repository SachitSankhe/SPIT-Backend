from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed, NotFound
from .models import Student, Branch
from .serializers import AuthStudentSerializer, StudentSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
# from .models import Committee
from django.db.utils import IntegrityError
import jwt
from django.conf import settings


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    # print(username, password)

    user = Student.objects.filter(email=email).first()

    try:
        instance = user
        user.id = str(user.id)
        user = AuthStudentSerializer(user).data
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


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'branch': request.POST.get('branch'),
        }

        committee_inst = StudentSerializer(data=data)

        if committee_inst.is_valid():
            try:
                instance = Student(name=data['name'], email=data['email'], password=make_password(
                    data['password']), branch=Branch.objects.get(id=data['branch']))
                # instance.password = make_password(data['password'])
                instance.save()
            except IntegrityError as e:
                return Response({
                    'detail': "User already present -> " + str(e)
                }, status=409)
            except:
                return Response({
                    'detail': "Some database error has occured."
                }, status=500)

            try:
                instance.id = str(instance.id)
                user = StudentSerializer(instance).data
                access_token = instance.getAccessToken()
                refresh_token = instance.getRefreshToken()
            except Exception as e:
                return Response({
                    'detail': "Error in serializing data or generating tokens -> Specific error is " + str(e)
                }, status=500)

            print('access_token => ', access_token)
            print('refresh_token => ', refresh_token)
            response = Response({
                'user': user,
                'access_token': access_token
            })
            response.set_cookie('jwt_refresh_token',
                                refresh_token, httponly=True)
            print(response)
            return response
        else:
            return Response({
                'details': committee_inst.errors
            })

@api_view(['GET'])
def refresh(request):
    refresh_token = request.COOKIES.get('jwt_refresh_token')
    if refresh_token is None:
        return Response({
            'detail': "No token present."
        }, status=406)
    user = Student.objects.filter(refreshToken=refresh_token).first()

    if user is None:
        return NotFound(detail="User not found", code=404)

    try:
        payload = jwt.decode(refresh_token, 'secret',
                             algorithms=[settings.ALGORITHM])
    except jwt.ExpiredSignatureError:
        return Response({
            'detail': "Token expired. Try again"
        }, status=403)
    except:
        return Response({
            'detail': "Some error occured."
        }, status=500)

    seralized_user = StudentSerializer(user).data

    if seralized_user.get('id') != payload.get('id'):
        return Response(status=403)

    access_token = user.getAccessToken()

    return Response({
        'access_token': access_token,
        'user': seralized_user
    })