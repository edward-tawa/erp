import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Category, CreateCategoryResponse, GetCategoryResponse } from "@/types/inventory/category.types";
import { createCategoryThunk } from "@/store/features/inventory/thunks/category.thunks";



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
            .addCase(createCategoryThunk.pending, (state) => {
                state.isLoading = true;
                state.isError = false;
            })
            .addCase(createCategoryThunk.fulfilled, (state, action: PayloadAction<GetCategoryResponse>) => {
                state.category = action.payload;
                state.isLoading = false;
                state.isError = false;
            })
            .addCase(createCategoryThunk.rejected, (state) => {
                state.isLoading = false;
                state.isError = true;
            })
            //==================================================
            //UPDATE CATEGORY
            //==================================================
            .addCase(createCategoryThunk.pending, (state) => {
                state.isLoading = true;
                state.isError = false;
            })
            .addCase(createCategoryThunk.fulfilled, (state, action: PayloadAction<Category>) => {
                state.category = action.payload;
                state.isLoading = false;
                state.isError = false;
            })
            .addCase(createCategoryThunk.rejected, (state) => {
                state.isLoading = false;
                state.isError = true;
            })

            //==================================================
            //DELETE CATEGORY
            //==================================================
            .addCase(createCategoryThunk.pending, (state) => {
                state.isLoading = true;
                state.isError = false;
            })
            .addCase(createCategoryThunk.fulfilled, (state, action: PayloadAction<Category>) => {
                state.category = action.payload;
                state.isLoading = false;
                state.isError = false;
            })
            .addCase(createCategoryThunk.rejected, (state) => {
                state.isLoading = false;
                state.isError = true;
            })

            //==================================================
            //UPDATE CATEGORY
            //==================================================
            .addCase(createCategoryThunk.pending, (state) => {
                state.isLoading = true;
                state.isError = false;
            })
            .addCase(createCategoryThunk.fulfilled, (state, action: PayloadAction<Category>) => {
                state.category = action.payload;
                state.isLoading = false;
                state.isError = false;
            })
            .addCase(createCategoryThunk.rejected, (state) => {
                state.isLoading = false;
                state.isError = true;
            })
    }
})

export const { setCategory, setLoading, setError, clearCategory } = categorySlice.actions;

export default categorySlice.reducer;