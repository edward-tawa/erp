import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { SalesOrderItem } from "@/types/sales/salesorderitem.types";

export interface SalesOrderItemState {
    salesOrderItem: SalesOrderItem | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: SalesOrderItemState = {
    salesOrderItem: null,
    isLoading: false,
    error: null,
}

const salesOrderItemSlice = createSlice({
    name: 'salesOrderItemSlice',
    initialState,
    reducers: {
        setSalesOrderItem: (state, action: PayloadAction<SalesOrderItem>) => {
            state.salesOrderItem = action.payload;
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

        clearSalesOrderItem: (state) => {
            state.salesOrderItem = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setSalesOrderItem, setLoading, setError, clearSalesOrderItem } = salesOrderItemSlice.actions;

export default salesOrderItemSlice.reducer;