import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { SalesOrderItem } from "@/types/sales/salesorderitem.types";

export interface SalesOrderItemsState {
    salesOrderItems: SalesOrderItem[] | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: SalesOrderItemsState = {
    salesOrderItems: null,
    isLoading: false,
    error: null,
}

const salesOrderItemsSlice = createSlice({
    name: 'salesOrderItemsSlice',
    initialState,
    reducers: {
        setSalesOrderItems: (state, action: PayloadAction<SalesOrderItem[]>) => {
            state.salesOrderItems = action.payload;
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

        clearSalesOrderItems: (state) => {
            state.salesOrderItems = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setSalesOrderItems, setLoading, setError, clearSalesOrderItems } = salesOrderItemsSlice.actions;

export default salesOrderItemsSlice.reducer;