from django.urls import path, include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.UserSignup.as_view(), name='signup'),
    path('mock/', views.mockView.as_view(), name='mock'),
    path('detail/', views.UserDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.UserDetail.as_view(), name='delete')
]
