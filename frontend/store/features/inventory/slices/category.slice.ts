import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Category, CreateCategoryResponse, GetCategoryResponse } from "@/types/inventory/category.types";
import { createCategoryThunk, getCategoryThunk, updateCategoryThunk, deleteCategoryThunk } from "@/store/features/inventory/thunks/category.thunks";



export interface CategoryState {
    category: Category | null;
    isLoading: boolean;
    isError: boolean;

}


const initialState: CategoryState = {
    category: null,
    isLoading: false,
    isError: false

}

export const categorySlice = createSlice({
    name: 'categorySlice',
    initialState,
    reducers: {
        setCategory: (state, action: PayloadAction<Category>) => {
            state.category = action.payload;
            state.isLoading = false;
            state.isError = false;
        },

        setLoading: (state, action: PayloadAction<boolean>) => {
            state.isLoading = action.payload;
        },

        setError: (state, action: PayloadAction<boolean>) => {
            state.isError = action.payload;
            state.isLoading = false;
        },

        clearCategory: (state) => {
            state.category = null;
            state.isLoading = false;
            state.isError = false;
        },
    },

    extraReducers: (builder) => {
        builder


            // ==================================================
            // CREATE CATEGORY
            // ==================================================
            .addCase(createCategoryThunk.pending, (state) => {
                state.isLoading = true;
                state.isError = false;
            })
            .addCase(createCategoryThunk.fulfilled, (state, action: PayloadAction<CreateCategoryResponse>) => {
                state.category = action.payload;
                state.isLoading = false;
                state.isError = false;
            })
            .addCase(createCategoryThunk.rejected, (state) => {
                state.isLoading = false;
                state.isError = true;
            })

            //==================================================
            //GET CATEGORY
            //==================================================
            .addCase(getCategoryThunk.pending, (state) => {
                state.isLoading = true;
                state.isError = false;
            })
            .addCase(getCategoryThunk.fulfilled, (state, action: PayloadAction<GetCategoryResponse>) => {
                state.category = action.payload;
                state.isLoading = false;
                state.isError = false;
            })
            //==================================================
            //UPDATE CATEGORY
            //==================================================
            .addCase(updateCategoryThunk.pending, (state) => {
                state.isLoading = true;
                state.isError = false;
            })
            .addCase(updateCategoryThunk.fulfilled, (state, action: PayloadAction<Category>) => {
                state.category = action.payload;
                state.isLoading = false;
                state.isError = false;
            })
            .addCase(updateCategoryThunk.rejected, (state) => {
                state.isLoading = false;
                state.isError = true;
            })

            //==================================================
            //DELETE CATEGORY
            //==================================================
            .addCase(deleteCategoryThunk.pending, (state) => {
                state.isLoading = true;
                state.isError = false;
            })
            .addCase(deleteCategoryThunk.fulfilled, (state, action: PayloadAction<number>) => {
                // If the deleted category is the one currently in state, clear it
                if (state.category && state.category.id === action.payload) {
                    state.category = null;
                }
                state.isLoading = false;
                state.isError = false;
            })
            .addCase(deleteCategoryThunk.rejected, (state) => {
                state.isLoading = false;
                state.isError = true;
            })
    }
})

export const { setCategory, setLoading, setError, clearCategory } = categorySlice.actions;

export default categorySlice.reducer;