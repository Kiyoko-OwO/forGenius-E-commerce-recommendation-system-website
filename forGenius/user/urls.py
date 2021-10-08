from django.urls import path
from user.views import *

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('send_reset_code/', send_reset_code, name='send_reset_code'),
    path('reset_password/', reset_password, name='reset_password'),
]
