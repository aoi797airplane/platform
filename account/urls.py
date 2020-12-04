from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.Login, name='login'),
    path('logout', views.log_out, name='logout'),
    path('info', views.user_info, name = 'user_info'),
]