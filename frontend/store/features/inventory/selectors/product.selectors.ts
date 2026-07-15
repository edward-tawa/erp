import { RootState } from "@/store/index";


export const selectProduct = (state: RootState) => state.product.product;


export const selectProductLoading = (state: RootState) => state.product.isLoading;