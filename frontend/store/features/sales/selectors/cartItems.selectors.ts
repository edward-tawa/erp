import { RootState } from "@/store";


export const selectCartItems = (state: RootState) => state.cartItems.cartItems;

export const selectCartItemsLoading = (state: RootState) => state.cartItems.isLoading;

export const selectCartItemsError = (state: RootState) => state.cartItems.error;


// 2. Compute the total quantity of all items in the cart
export const selectCartTotalQuantity = (state: RootState) => {
    const items = state.cartItems.cartItems;
    if (!items) return 0;

    // Sum up the quantity from each CartItem
    return items.reduce((total, item) => total + item.quantity, 0);
};