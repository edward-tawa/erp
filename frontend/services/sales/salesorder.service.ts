import api from "@/services/api";
import { SalesOrder, CreateSalesOrderRequest, CreateSalesOrderResponse } from "@/types/sales/salesorder.types";

const salesOrderService = {
    createSalesOrder: async (salesOrder: CreateSalesOrderRequest): Promise<CreateSalesOrderResponse> => {
        const response = await api.post<CreateSalesOrderResponse>("/sales-orders", salesOrder);
        return response.data;
    },

    getSalesOrder: async (id: number): Promise<SalesOrder> => {
        const response = await api.get<SalesOrder>(`/sales-orders/${id}`);
        return response.data;
    },

    updateSalesOrder: async (id: number, salesOrder: CreateSalesOrderRequest): Promise<SalesOrder> => {
        const response = await api.put<SalesOrder>(`/sales-orders/${id}`, salesOrder);
        return response.data;
    },

    deleteSalesOrder: async (id: number): Promise<void> => {
        await api.delete(`/sales-orders/${id}`);
    },
}

export default salesOrderService;