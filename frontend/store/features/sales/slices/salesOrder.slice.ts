import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { SalesOrder } from "@/types/sales/salesorder.types";

export interface SalesOrderState {
    salesOrder: SalesOrder | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: SalesOrderState = {
    salesOrder: null,
    isLoading: false,
    error: null,
}

const salesOrderSlice = createSlice({
    name: 'salesOrderSlice',
    initialState,
    reducers: {
        setSalesOrder: (state, action: PayloadAction<SalesOrder>) => {
            state.salesOrder = action.payload;
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

        clearSalesOrder: (state) => {
            state.salesOrder = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setSalesOrder, setLoading, setError, clearSalesOrder } = salesOrderSlice.actions;

export default salesOrderSlice.reducer;