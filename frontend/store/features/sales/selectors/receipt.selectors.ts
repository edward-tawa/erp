import { RootState } from "@/store";


export const selectReceiptState = (state: RootState) => state.receipt.receipt;

export const selectReceiptLoading = (state: RootState) => state.receipt.isLoading;

export const selectReceiptError = (state: RootState) => state.receipt.error;