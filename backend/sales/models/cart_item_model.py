from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models


class CartItem(CreatedUpdatedAt):
    cart = models.ForeignKey(
        "sales.Cart",
        on_delete=models.CASCADE,
        related_name="cart_items",
        help_text="The cart this item belongs to",
    )

    product = models.ForeignKey(
        "inventory.Product",
        on_delete=models.CASCADE,
        related_name="cart_items",
        help_text="The product added to the cart",
    )

    sales_order_item = models.OneToOneField(
        "sales.SalesOrderItem",
        on_delete=models.SET_NULL,
        related_name="cart_item",
        null=True,
        blank=True,
        help_text="The sales order item created from this cart item (if any)",
    )

    quantity = models.PositiveIntegerField(
        help_text="Quantity of the product in the cart"
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Unit price of the product in the cart",
    )

    @property
    def subtotal(self):
        return self.quantity * self.unit_price

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cart.update_cart_total()

    def delete(self, *args, **kwargs):
        cart = self.cart
        super().delete(*args, **kwargs)
        cart.update_cart_total()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart for {self.cart.user.username}"

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

        indexes = [
            models.Index(fields=["cart"]),
            models.Index(fields=["product"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["product", "cart"], name="unique_product_in_cart"
            )
        ]
