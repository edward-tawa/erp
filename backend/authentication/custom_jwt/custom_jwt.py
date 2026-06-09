from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from loguru import logger


class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT authentication that reads tokens from cookies instead of headers.
    """

    def authenticate(self, request):
        """
        Overrides the default JWT authentication to add logging and handle edge cases.
        """
        # Get token from cookie instead of Authorization header
        access_token = request.COOKIES.get("access_token")

        if not access_token:
            # Try the default Authorization header as fallback
            auth_header = request.headers.get("Authorization")
            if auth_header and auth_header.startswith("Bearer "):
                access_token = auth_header.split(" ")[1]
            else:
                logger.debug("JWT authentication: No token found in cookies or headers")
                return None

        try:
            # Validate the token
            validated_token = self.get_validated_token(access_token)

            # Get the user from the token
            user = self.get_user(validated_token)

            logger.info(
                f"JWT authentication successful for user: {user.email if user else 'Unknown'}"
            )
            return (user, validated_token)

        except InvalidToken as e:
            logger.warning(f"JWT authentication failed - Invalid token: {str(e)}")
            return None
        except TokenError as e:
            logger.warning(f"JWT authentication failed - Token error: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"JWT authentication error - Unexpected: {str(e)}")
            return None

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the WWW-Authenticate header
        in a 401 Unauthorized response.
        """
        return 'Bearer realm="api"'
