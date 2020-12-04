from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ea', views.ea, name ='ea'),
    path('ea/request', views.ea_request, name='request'),
    path('terms_of_service', views.termsofservice, name = 'terms_of_service' ),
    path('privacy_policy', views.privacypolicy, name = 'privacy_policy'),
    path('how_to_use', views.how_to_use, name = 'how_to_use'),
    
]