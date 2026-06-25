import api from "@/services/api";
import { CreateSalesOrderItemRequest, CreateSalesOrderItemResponse, GetSalesOrderItemResponse } from "@/types/sales/salesorderitem.types";

const salesOrderItemService = {
    createSalesOrderItem: async (salesOrderItem: CreateSalesOrderItemRequest): Promise<CreateSalesOrderItemResponse> => {
        const response = await api.post<CreateSalesOrderItemResponse>("/sales-order-items", salesOrderItem);
        return response.data;
    },

    getSalesOrderItem: async (id: number): Promise<GetSalesOrderItemResponse> => {
        const response = await api.get<GetSalesOrderItemResponse>(`/sales-order-items/${id}`);
        return response.data;
    },

    updateSalesOrderItem: async (id: number, salesOrderItem: CreateSalesOrderItemRequest): Promise<GetSalesOrderItemResponse> => {
        const response = await api.put<GetSalesOrderItemResponse>(`/sales-order-items/${id}`, salesOrderItem);
        return response.data;
    },

    deleteSalesOrderItem: async (id: number): Promise<void> => {
        await api.delete(`/sales-order-items/${id}`);
    },
}

export default salesOrderItemService;