import { createAsyncThunk } from "@reduxjs/toolkit";
import { Product } from "@/types/inventory/product.types";
import { productService } from "@/services/inventory/product.service";

// 1. CREATE
export const createProductsThunk = createAsyncThunk(
    'products/create',
    async (products: Product[], thunkAPI) => {
        try {
            const response = await Promise.all(products.map(product => productService.createProduct(product)));
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);

// 2. READ
export const getProductsThunk = createAsyncThunk(
    'products/get',
    async (ids: number[], thunkAPI) => {
        try {
            const response = await Promise.all(ids.map(id => productService.getProduct(id)));
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);

// 3. UPDATE
export const updateProductsThunk = createAsyncThunk(
    'products/update',
    async ({ id, product }: { id: number; product: Product }, thunkAPI) => {
        try {
            const response = await productService.updateProduct(id, product);
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);

// 4. DELETE
export const deleteProductsThunk = createAsyncThunk(
    'products/delete',
    async (id: number, thunkAPI) => {
        try {
            const response = await productService.deleteProduct(id);
            return response; // You might want to return `id` here so your reducer knows what to remove
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);