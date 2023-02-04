from django.urls import path
from faculty.models import login

app_name = 'committee'

urlpatterns = [
    path('/committee/login', login, name='committee-login')
]
