from django.urls import path
from committee.views import login,register,refresh

app_name = 'committee'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('refresh/', refresh, name='refresh')
]
