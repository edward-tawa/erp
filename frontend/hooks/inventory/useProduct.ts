import { useDispatch, useSelector } from "react-redux";
import { AppDispatch } from "@/store/index";
import { selectProduct, selectProductLoading } from "@/store/features/inventory/selectors/product.selectors";
import { setError, clearProduct } from "@/store/features/inventory/slices/product.slice";
import { Product } from "@/types/inventory/product.types";
import {
    createProductThunk,
    getProductThunk,
    updateProductThunk,
    deleteProductThunk
} from "@/store/features/inventory/thunks/product.thunks";

export const useProduct = () => {
    const dispatch: AppDispatch = useDispatch();
    const product = useSelector(selectProduct);
    const isLoading = useSelector(selectProductLoading);


    const handleCreateProduct = async (productData: Product) => {
        try {

            return await dispatch(createProductThunk(productData)).unwrap();
        } catch (error) {
            console.error("Error during creating product:", error);
            throw error;
        }
    };


    const handleGetProduct = async (productId: number) => {
        try {
            return await dispatch(getProductThunk(productId)).unwrap();
        } catch (error) {
            console.error("Error during fetching product:", error);
            throw error;
        }
    };


    const handleUpdateProduct = async ({ id, product: productData }: { id: number; product: Product }) => {
        try {
            return await dispatch(updateProductThunk({ id, product: productData })).unwrap();
        } catch (error) {
            console.error("Error during updating product:", error);
            throw error;
        }
    };


    const handleDeleteProduct = async (productId: number) => {
        try {
            return await dispatch(deleteProductThunk(productId)).unwrap();
        } catch (error) {
            console.error("Error during deleting product:", error);
            throw error;
        }
    };


    const handleSetError = (error: string | null) => {
        dispatch(setError(error));
    };

    const handleClearProduct = () => {
        dispatch(clearProduct());
    };

    return {
        product,
        isLoading,
        handleCreateProduct,
        handleGetProduct,
        handleUpdateProduct,
        handleDeleteProduct,
        handleSetError,
        handleClearProduct
    };
};