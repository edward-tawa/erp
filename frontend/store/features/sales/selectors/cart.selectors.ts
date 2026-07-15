import { RootState } from "@/store";

export const selectCart = (state: RootState) => state.cart.cart;

export const selectCartLoading = (state: RootState) => state.cart.isLoading;

export const selectCartError = (state: RootState) => state.cart.error;