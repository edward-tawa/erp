import { RootState } from "@/store";


export const selectCartItem = (state: RootState) => state.cartItem.cartItem;


export const selectCartItemLoading = (state: RootState) => state.cartItem.isLoading;


export const selectCartItemError = (state: RootState) => state.cartItem.error;


export const selectCartItemById = (state: RootState, id: number) => {
    const cartItem = state.cartItem.cartItem;
    if (cartItem && cartItem.id === id) {
        return cartItem;
    }
    return null;
}


export const selectCartItemByProductName = (state: RootState, productName: string) => {
    const cartItem = state.cartItem.cartItem;
    if (cartItem && cartItem.product.name === productName) {
        return cartItem;
    }
    return null;
}