from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.middleware.csrf import get_token
from users.serializers.user_serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import Q
from loguru import logger

User = get_user_model()


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer = UserSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = User.objects.filter(Q(email=username) | Q(username=username)).first()
            if user and user.check_password(password):
                if not user.is_active:
                    logger.warning(f"Login failed: Inactive account '{username}'")
                    return Response(
                        {"error": "Account is inactive."},
                        status=status.HTTP_403_FORBIDDEN,
                    )

                refresh_token = RefreshToken.for_user(user)
                access_token = str(refresh_token.access_token)
                logger.info(f"User '{user.email}' logged in successfully")
                response = Response(
                    {"message": "Login successful"}, status=status.HTTP_200_OK
                )

                get_token(request)  # Ensure CSRF token is set

                response.set_cookie(
                    key="refresh_token",
                    value=str(refresh_token),
                    httponly=True,
                    secure=True,
                    samesite="Strict",
                    path="/api/auth/refresh/",
                    max_age=60 * 60 * 24 * 7,
                )

                response.set_cookie(
                    key="access_token",
                    value=access_token,
                    httponly=True,
                    secure=True,
                    samesite="Strict",
                    path="/",
                    max_age=60 * 15 * 2,
                )
                return response
            else:
                logger.warning(f"Login failed: Invalid credentials for '{username}'")
                return Response(
                    {"error": "Invalid username or password."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
