import { configureStore } from "@reduxjs/toolkit";
import authReducer from "@/store/features/auth/auth.slice";
import cartReducer from "@/store/features/sales/slices/cart.slice";
import cartItemReducer from "@/store/features/sales/slices/cartItem.slice";
import cartItemsReducer from "@/store/features/sales/slices/cartItems.slice";
import receiptReducer from "@/store/features/sales/slices/receipt.slice";
import receiptItemReducer from "@/store/features/sales/slices/receiptItem.slice";
import receiptItemsReducer from "@/store/features/sales/slices/receiptItems.slice";
import salesOrderReducer from "@/store/features/sales/slices/salesOrder.slice";
import salesOrderItemReducer from "@/store/features/sales/slices/salesOrderItem.slice";
import salesOrderItemsReducer from "@/store/features/sales/slices/salesOrderItems.slice";
import checkoutReducer from "@/store/features/sales/slices/checkout.slice";
import paymentReducer from "@/store/features/sales/slices/payment.slice";
import productReducer from "@/store/features/inventory/slices/product.slice";
import productsReducer from "@/store/features/inventory/slices/products.slice";
import categoryReducer from "@/store/features/inventory/slices/category.slice"

export const store = configureStore({
    reducer: {
        auth: authReducer,
        salesOrder: salesOrderReducer,
        salesOrderItem: salesOrderItemReducer,
        salesOrderItems: salesOrderItemsReducer,
        cart: cartReducer,
        cartItem: cartItemReducer,
        cartItems: cartItemsReducer,
        receipt: receiptReducer,
        receiptItem: receiptItemReducer,
        receiptItems: receiptItemsReducer,
        checkout: checkoutReducer,
        payment: paymentReducer,
        product: productReducer,
        products: productsReducer,
        category: categoryReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;