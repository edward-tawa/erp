import { RootState } from "@/store";


export const selectCartItemsState = (state: RootState) => state.cartItems.cartItems;

export const selectCartItemsLoading = (state: RootState) => state.cartItems.isLoading;

export const selectCartItemsError = (state: RootState) => state.cartItems.error;