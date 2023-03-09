from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views.authentication.login import UserLogin
from .views.authentication.logout import LogoutView


urlpatterns = [

    path('login/', UserLogin.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
]
