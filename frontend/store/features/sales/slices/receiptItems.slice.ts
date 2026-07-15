import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { ReceiptItem } from "@/types/sales/receiptitem.types";

export interface ReceiptItemsState {
    receiptItems: ReceiptItem[] | null;
    isLoading: boolean;
    error: string | null;
}


const initialState: ReceiptItemsState = {
    receiptItems: null,
    isLoading: false,
    error: null,
}

const receiptItemsSlice = createSlice({
    name: 'receiptItemsSlice',
    initialState,
    reducers: {
        setReceiptItems: (state, action: PayloadAction<ReceiptItem[]>) => {
            state.receiptItems = action.payload;
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

        clearReceiptItems: (state) => {
            state.receiptItems = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setReceiptItems, setLoading, setError, clearReceiptItems } = receiptItemsSlice.actions;

export default receiptItemsSlice.reducer;