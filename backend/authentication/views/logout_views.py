from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from authentication.custom_jwt.custom_jwt import CustomJWTAuthentication
from loguru import logger

User = get_user_model()


class LogoutView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            logger.warning(
                f"Logout attempted without refresh token for user: {request.user.username}"
            )
            # Still clear cookies and return success
            response = Response(
                {"message": "Logout successful"}, status=status.HTTP_200_OK
            )
            response.delete_cookie("refresh_token", path="/api/auth/refresh/")
            response.delete_cookie("access_token", path="/")
            return response

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"Refresh token blacklisted for user: {request.user.username}")

            # Create success response
            response = Response(
                {"message": "Logout successful"}, status=status.HTTP_200_OK
            )

        except TokenError as e:
            logger.warning(
                f"Invalid token during logout for user {request.user.username}: {str(e)}"
            )
            # Still return success but log the error
            response = Response(
                {"message": "Logout successful"}, status=status.HTTP_200_OK
            )

        # Clear cookies in all cases
        response.delete_cookie("refresh_token", path="/api/auth/refresh/")
        response.delete_cookie("access_token", path="/")

        logger.info(f"User '{request.user.username}' logged out successfully")
        return response
