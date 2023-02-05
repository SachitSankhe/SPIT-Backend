from django.urls import path
from faculty.views import login, register,refresh

app_name = 'faculty'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('refresh/', refresh, name='refresh')

]
