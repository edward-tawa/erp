import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Receipt } from "@/types/sales/receipt.types";

export interface ReceiptState {
    receipt: Receipt | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: ReceiptState = {
    receipt: null,
    isLoading: false,
    error: null,
}

const receiptSlice = createSlice({
    name: 'receiptSlice',
    initialState,
    reducers: {
        setReceipt: (state, action: PayloadAction<Receipt>) => {
            state.receipt = action.payload;
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

        clearReceipt: (state) => {
            state.receipt = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setReceipt, setLoading, setError, clearReceipt } = receiptSlice.actions;

export default receiptSlice.reducer;