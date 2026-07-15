import { createAsyncThunk } from "@reduxjs/toolkit";
import { categoryService } from "@/services/inventory/category.service";
import { Category } from "@/types/inventory/category.types";


export const createCategoryThunk = createAsyncThunk(
    'categories/create',
    async (category: Category, thunkAPI) => {
        try {
            const response = await categoryService.createCategory(category);
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);



export const getCategoryThunk = createAsyncThunk(
    'categories/get',
    async (name: string, thunkAPI) => {
        try {
            const response = await categoryService.getCategory(name);
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);



export const updateCategoryThunk = createAsyncThunk(
    'categories/update',
    async ({ id, category }: { id: number; category: Category }, thunkAPI) => {
        try {
            const response = await categoryService.updateCategory(id, category);
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);




export const deleteCategoryThunk = createAsyncThunk(
    'categories/delete',
    async (id: number, thunkAPI) => {
        try {
            await categoryService.deleteCategory(id);
            return id; // Return the deleted category ID for the reducer to handle
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
);