import { createAsyncThunk } from "@reduxjs/toolkit";
import { productService } from "@/services/inventory/product.service";
import { Product } from "@/types/inventory/product.types";

// 1. CREATE
export const createProductThunk = createAsyncThunk(
    'products/create',
    async (product: Product, thunkAPI) => {
        try {
            const response = await productService.createProduct(product);
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);

// 2. READ
export const getProductThunk = createAsyncThunk(
    'products/get',
    async (id: number, thunkAPI) => {
        try {
            const response = await productService.getProduct(id);
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);

// 3. UPDATE
export const updateProductThunk = createAsyncThunk(
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
export const deleteProductThunk = createAsyncThunk(
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