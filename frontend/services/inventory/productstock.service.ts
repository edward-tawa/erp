import api from "@/services/api";
import { ProductStock, CreateProductStockRequest, CreateProductStockResponse } from "@/types/inventory/productstock.types";



const productStockService = {
    createProductStock: async (productStock: CreateProductStockRequest): Promise<CreateProductStockResponse> => {
        const response = await api.post<CreateProductStockResponse>("/product-stocks", productStock);
        return response.data;
    },

    getProductStock: async (id: number): Promise<ProductStock> => {
        const response = await api.get<ProductStock>(`/product-stocks/${id}`);
        return response.data;
    },

    updateProductStock: async (id: number, productStock: CreateProductStockRequest): Promise<ProductStock> => {
        const response = await api.put<ProductStock>(`/product-stocks/${id}`, productStock);
        return response.data;
    },

    deleteProductStock: async (id: number): Promise<void> => {
        await api.delete(`/product-stocks/${id}`);
    },
}

export default productStockService;