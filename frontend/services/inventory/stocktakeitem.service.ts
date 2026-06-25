import api from "@/services/api";
import { StocktakeItem, CreateStocktakeItemRequest, CreateStocktakeItemResponse } from "@/types/inventory/stocktakeitem.types";

const stocktakeItemService = {
    createStocktakeItem: async (stocktakeItem: CreateStocktakeItemRequest): Promise<CreateStocktakeItemResponse> => {
        const response = await api.post<CreateStocktakeItemResponse>("/stocktake-items", stocktakeItem);
        return response.data;
    },

    getStocktakeItem: async (id: number): Promise<StocktakeItem> => {
        const response = await api.get<StocktakeItem>(`/stocktake-items/${id}`);
        return response.data;
    },

    updateStocktakeItem: async (id: number, stocktakeItem: CreateStocktakeItemRequest): Promise<StocktakeItem> => {
        const response = await api.put<StocktakeItem>(`/stocktake-items/${id}`, stocktakeItem);
        return response.data;
    },

    deleteStocktakeItem: async (id: number): Promise<void> => {
        await api.delete(`/stocktake-items/${id}`);
    },
}

export default stocktakeItemService;