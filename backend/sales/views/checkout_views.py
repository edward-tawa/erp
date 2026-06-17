from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sales.serializers.checkout_serializer import CheckoutSerializer
from sales.services.check_out_service import CheckOutService
from sales.models.cart_model import Cart
from users.permissions.user_permissions import IsEmployee, IsManager


class CheckoutView(APIView):
    permission_classes = [IsEmployee | IsManager]

    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            cart = serializer.validated_data["cart"]
            customer = serializer.validated_data["customer"]
            notes = serializer.validated_data.get("notes", None)

            try:
                cart = Cart.objects.get(id=cart)
            except Cart.DoesNotExist:
                return Response(
                    {"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND
                )

            checkout_result = CheckOutService.checkout_cart(
                cart=cart, user=request.user, customer=customer, notes=notes
            )
            return Response(checkout_result, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
