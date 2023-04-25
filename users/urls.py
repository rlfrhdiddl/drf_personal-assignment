from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.sign_up, name='signup')
]
