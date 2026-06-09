from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from loguru import logger


class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom view to handle token refresh and set new access token in cookies.
    """

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            logger.warning("Token refresh attempted without refresh token in cookies")
            return Response(
                {"error": "Refresh token not provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Manually construct the data for the serializer
        data = {"refresh": refresh_token}
        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            logger.warning(f"Token refresh failed - Invalid token: {str(e)}")
            return Response(
                {"error": "Invalid refresh token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        access_token = serializer.validated_data.get("access")
        logger.info("Access token refreshed successfully")

        response = Response(
            {"message": "Token refreshed successfully"}, status=status.HTTP_200_OK
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
