import api from "@/services/api";
import { CreateCategoryRequest, CreateCategoryResponse } from "@/types/inventory/category.types";


const categoryService = {
    createCategory: async (category: CreateCategoryRequest): Promise<CreateCategoryResponse> => {
        const response = await api.post<CreateCategoryResponse>("/categories", category);
        return response.data;
    },

    getCategory: async (name: string): Promise<CreateCategoryResponse> => {
        const response = await api.get<CreateCategoryResponse>(`/categories/${name}`);
        return response.data;
    },

    updateCategory: async (id: number, category: CreateCategoryRequest): Promise<CreateCategoryResponse> => {
        const response = await api.put<CreateCategoryResponse>(`/categories/${id}`, category);
        return response.data;
    },

    deleteCategory: async (id: number): Promise<void> => {
        await api.delete(`/categories/${id}`);
    },
}

export default categoryService;