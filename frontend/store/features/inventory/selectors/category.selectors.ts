import { RootState } from "@/store/index";


export const selectCategoryState = (state: RootState) => state.category.category;

export const selectIsLoadingState = (state: RootState) => state.category.isLoading;

export const selectIsErrorState = (state: RootState) => state.category.isError;


