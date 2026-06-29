import api from "@/services/api";
import { ReceiptItem, CreateReceiptItemRequest, CreateReceiptItemResponse } from "@/types/sales/receiptitem.types";

const receiptItemService = {
    createReceiptItem: async (receiptItem: CreateReceiptItemRequest): Promise<CreateReceiptItemResponse> => {
        const response = await api.post<CreateReceiptItemResponse>("/receipt-items", receiptItem);
        return response.data;
    },

    getReceiptItem: async (id: number): Promise<ReceiptItem> => {
        const response = await api.get<ReceiptItem>(`/receipt-items/${id}`);
        return response.data;
    },

    updateReceiptItem: async (id: number, receiptItem: CreateReceiptItemRequest): Promise<ReceiptItem> => {
        const response = await api.put<ReceiptItem>(`/receipt-items/${id}`, receiptItem);
        return response.data;
    },

    deleteReceiptItem: async (id: number): Promise<void> => {
        await api.delete(`/receipt-items/${id}`);
    },
}

export default receiptItemService;