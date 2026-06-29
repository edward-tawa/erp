import api from "@/services/api";
import {
    Product,
    CreateProductRequest,
    CreateProductResponse,
    GetProductRequest,
    UpdateProductRequest,
    UpdateProductResponse,
    DeleteProductRequest,
    DeleteProductResponse,
    GetProductResponse
} from "@/types/inventory/product.types";

const productService = {
    createProduct: async (product: CreateProductRequest): Promise<CreateProductResponse> => {
        const response = await api.post<CreateProductResponse>("/products", product);
        return response.data;
    },

    getProduct: async (id: number): Promise<GetProductResponse> => {
        const response = await api.get<GetProductResponse>(`/products/${id}`);
        return response.data;
    },

    updateProduct: async (id: number, product: UpdateProductRequest): Promise<UpdateProductResponse> => {
        const response = await api.put<UpdateProductResponse>(`/products/${id}`, product);
        return response.data;
    },

    deleteProduct: async (id: number): Promise<DeleteProductResponse> => {
        const response = await api.delete<DeleteProductResponse>(`/products/${id}`);
        return response.data;
    },
}


