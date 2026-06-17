from django.urls import path

from authentication.views.login_views import LoginView
from authentication.views.logout_views import LogoutView
from authentication.views.refresh_token_views import CustomTokenRefreshView
from authentication.views.signup_views import SignupView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("refresh/", CustomTokenRefreshView.as_view(), name="refresh"),
]
