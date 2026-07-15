import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Product, CreateProductResponse } from "@/types/inventory/product.types";
import { createProductThunk, getProductThunk, updateProductThunk, deleteProductThunk } from "@/store/features/inventory/thunks/product.thunks";



export interface ProductState {
    product: Product | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: ProductState = {
    product: null,
    isLoading: false,
    error: null,
}

const productSlice = createSlice({
    name: 'productSlice',
    initialState,
    reducers: {
        setProduct: (state, action: PayloadAction<Product>) => {
            state.product = action.payload;
            state.isLoading = false;
            state.error = null;
        },

        addProduct: (state, action: PayloadAction<Product>) => {
            state.product = action.payload;
            state.isLoading = false;
            state.error = null;
        },

        updateProduct: (state, action: PayloadAction<Product>) => {
            state.product = action.payload;
            state.isLoading = false;
            state.error = null;
        },

        deleteProduct: (state) => {
            state.product = null;
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

        clearProduct: (state) => {
            state.product = null;
            state.isLoading = false;
            state.error = null;
        },
    },

    extraReducers: (builder) => {
        builder
            // =============================================
            // CREATE PRODUCT
            // =============================================
            .addCase(createProductThunk.pending, (state) => {
                state.isLoading = true;
                state.error = null;
            })
            .addCase(createProductThunk.fulfilled, (state, action: PayloadAction<CreateProductResponse>) => {
                state.product = action.payload;
                state.isLoading = false;
                state.error = null;
            })
            .addCase(createProductThunk.rejected, (state, action: PayloadAction<any>) => {
                state.isLoading = false;
                state.error = action.payload;
            })
            // =============================================
            // GET PRODUCT
            // =============================================
            .addCase(getProductThunk.pending, (state) => {
                state.isLoading = true;
                state.error = null;
            })
            .addCase(getProductThunk.fulfilled, (state, action: PayloadAction<Product>) => {
                state.product = action.payload;
                state.isLoading = false;
                state.error = null;
            })
            .addCase(getProductThunk.rejected, (state, action: PayloadAction<any>) => {
                state.isLoading = false;
                state.error = action.payload;
            })
            // =============================================
            // UPDATE PRODUCT
            // =============================================
            .addCase(updateProductThunk.pending, (state) => {
                state.isLoading = true;
                state.error = null;
            })
            .addCase(updateProductThunk.fulfilled, (state, action: PayloadAction<Product>) => {
                state.product = action.payload;
                state.isLoading = false;
                state.error = null;
            })
            .addCase(updateProductThunk.rejected, (state, action: PayloadAction<any>) => {
                state.isLoading = false;
                state.error = action.payload;
            })
            // =============================================
            // DELETE PRODUCT
            // =============================================
            .addCase(deleteProductThunk.pending, (state) => {
                state.isLoading = true;
                state.error = null;
            })
            .addCase(deleteProductThunk.fulfilled, (state) => {
                state.product = null;
                state.isLoading = false;
                state.error = null;
            })
            .addCase(deleteProductThunk.rejected, (state, action: PayloadAction<any>) => {
                state.isLoading = false;
                state.error = action.payload;
            })
    },
})

export const { setProduct, setLoading, setError, clearProduct, addProduct, updateProduct, deleteProduct } = productSlice.actions;

export default productSlice.reducer;