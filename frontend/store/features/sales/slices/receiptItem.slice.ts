import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { ReceiptItem } from "@/types/sales/receiptitem.types";


export interface ReceiptItemState {
    receiptItem: ReceiptItem | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: ReceiptItemState = {
    receiptItem: null,
    isLoading: false,
    error: null,
}

const receiptItemSlice = createSlice({
    name: 'receiptItemSlice',
    initialState,
    reducers: {
        setReceiptItem: (state, action: PayloadAction<ReceiptItem>) => {
            state.receiptItem = action.payload;
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

        clearReceiptItem: (state) => {
            state.receiptItem = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setReceiptItem, setLoading, setError, clearReceiptItem } = receiptItemSlice.actions;

export default receiptItemSlice.reducer;