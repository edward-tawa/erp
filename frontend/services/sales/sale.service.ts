import api from "@/services/api";
import { Sale, CreateSaleRequest, CreateSaleResponse } from "@/types/sales/sale.types";

const saleService = {
    createSale: async (sale: CreateSaleRequest): Promise<CreateSaleResponse> => {
        const response = await api.post<CreateSaleResponse>("/sales", sale);
        return response.data;
    },

    getSale: async (id: number): Promise<Sale> => {
        const response = await api.get<Sale>(`/sales/${id}`);
        return response.data;
    },

    updateSale: async (id: number, sale: CreateSaleRequest): Promise<Sale> => {
        const response = await api.put<Sale>(`/sales/${id}`, sale);
        return response.data;
    },

    deleteSale: async (id: number): Promise<void> => {
        await api.delete(`/sales/${id}`);
    },
}

export default saleService;