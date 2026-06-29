import api from "@/services/api";
import { CreateStocktakeRequest, CreateStocktakeResponse, GetStocktakeResponse } from "@/types/inventory/stocktake.types";

const stocktakeService = {
    createStocktake: async (stocktake: CreateStocktakeRequest): Promise<CreateStocktakeResponse> => {
        const response = await api.post<CreateStocktakeResponse>("/stocktakes", stocktake);
        return response.data;
    },

    getStocktake: async (id: number): Promise<GetStocktakeResponse> => {
        const response = await api.get<GetStocktakeResponse>(`/stocktakes/${id}`);
        return response.data;
    },
}

export default stocktakeService;