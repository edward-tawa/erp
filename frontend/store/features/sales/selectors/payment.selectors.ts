import { RootState } from "@/store";



export const selectPaymentState = (state: RootState) => state.payment.payment;

export const selectPaymentLoading = (state: RootState) => state.payment.isLoading;

export const selectPaymentError = (state: RootState) => state.payment.error;