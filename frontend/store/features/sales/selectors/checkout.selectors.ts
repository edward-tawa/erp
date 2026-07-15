import { RootState } from "@/store";



export const selectCheckoutState = (state: RootState) => state.checkout.checkout;

export const selectCheckoutLoading = (state: RootState) => state.checkout.isLoading;

export const selectCheckoutError = (state: RootState) => state.checkout.error;