from django.urls import path
from .views import login, register, refresh


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('refresh/', refresh, name='refresh')
]
