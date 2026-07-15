import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Product } from "@/types/inventory/product.types";

export interface ProductsState {
    products: Product[];
    isLoading: boolean;
    error: string | null;
}

const initialState: ProductsState = {
    products: [],
    isLoading: false,
    error: null,
}

const productsSlice = createSlice({
    name: 'productsSlice',
    initialState,
    reducers: {
        setProducts: (state, action: PayloadAction<Product[]>) => {
            state.products = action.payload;
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

        clearProducts: (state) => {
            state.products = [];
            state.isLoading = false;
            state.error = null;
        },
    }
})

export const { setProducts, setLoading, setError, clearProducts } = productsSlice.actions;

export default productsSlice.reducer;