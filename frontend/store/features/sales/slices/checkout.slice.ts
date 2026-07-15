import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Checkout } from "@/types/sales/checkout.types";

export interface CheckoutState {
    checkout: Checkout | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: CheckoutState = {
    checkout: null,
    isLoading: false,
    error: null,
}

const checkoutSlice = createSlice({
    name: 'checkoutSlice',
    initialState,
    reducers: {
        setCheckout: (state, action: PayloadAction<Checkout>) => {
            state.checkout = action.payload;
            state.isLoading = false;
            state.error = null;
        },

        setLoading: (state, action: PayloadAction<boolean>) => {
            state.isLoading = action.payload;
        },

        setError: (state, action: PayloadAction<string | null>) => {
            state.error = action.payload;
            state.isLoading = false;
        },

        clearCheckout: (state) => {
            state.checkout = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setCheckout, setLoading, setError, clearCheckout } = checkoutSlice.actions;

export default checkoutSlice.reducer;