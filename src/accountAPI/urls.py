from django.urls import path
from django.conf.urls import include
from accountAPI.views import (
	UserRegistration,
)
from rest_framework_simplejwt import views as jwt_views

app_name = 'accountAPI'

urlpatterns = [
	path('register', UserRegistration, name="register"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]