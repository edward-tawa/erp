import { RootState } from "@/store";

export const selectProductsState = (state: RootState) => state.products.products;

export const selectProductsLoading = (state: RootState) => state.products.isLoading;

export const selectProductsError = (state: RootState) => state.products.error;