import api from "@/services/api";
import { Receipt, CreateReceiptRequest, CreateReceiptResponse } from "@/types/sales/receipt.types";

const receiptService = {
    createReceipt: async (receipt: CreateReceiptRequest): Promise<CreateReceiptResponse> => {
        const response = await api.post<CreateReceiptResponse>("/receipts", receipt);
        return response.data;
    },

    getReceipt: async (id: number): Promise<Receipt> => {
        const response = await api.get<Receipt>(`/receipts/${id}`);
        return response.data;
    },

    updateReceipt: async (id: number, receipt: CreateReceiptRequest): Promise<Receipt> => {
        const response = await api.put<Receipt>(`/receipts/${id}`, receipt);
        return response.data;
    },

    deleteReceipt: async (id: number): Promise<void> => {
        await api.delete(`/receipts/${id}`);
    },
}

export default receiptService;