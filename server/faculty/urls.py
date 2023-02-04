from django.urls import path
from faculty.models import login

app_name = 'faculty'

urlpatterns = [
    path('faculty/login/', login, name='faculty-login')
]
