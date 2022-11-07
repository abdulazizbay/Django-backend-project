from django.urls import path
from .views import *

urlpatterns = [
    # Auth
    path('log_in/', log_in, name='log_in'),
    path('register/', register, name='register'),
    path('verify/', verify, name='verify'),
    path('log_out/', log_out, name='log_out'),

]
