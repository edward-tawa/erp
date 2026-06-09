from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers.user_serializer import UserSerializer
from rest_framework.permissions import AllowAny
from loguru import logger


class SignupView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f"New user '{user.email}' signed up successfully.")
            return Response(
                {"message": "User created successfully."},
                status=status.HTTP_201_CREATED,
            )
        else:
            logger.warning(f"Signup failed with errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
