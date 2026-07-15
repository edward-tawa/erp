import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Payment } from "@/types/sales/payment.types";

export interface PaymentState {
    payment: Payment | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: PaymentState = {
    payment: null,
    isLoading: false,
    error: null,
}

const paymentSlice = createSlice({
    name: 'paymentSlice',
    initialState,
    reducers: {
        setPayment: (state, action: PayloadAction<Payment>) => {
            state.payment = action.payload;
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

        clearPayment: (state) => {
            state.payment = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setPayment, setLoading, setError, clearPayment } = paymentSlice.actions;

export default paymentSlice.reducer;                            