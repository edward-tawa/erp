import api from "@/services/api";
import { Payment, CreatePaymentRequest, CreatePaymentResponse } from "@/types/sales/payment.types";

const paymentService = {
    createPayment: async (payment: CreatePaymentRequest): Promise<CreatePaymentResponse> => {
        const response = await api.post<CreatePaymentResponse>("/payments", payment);
        return response.data;
    },

    getPayment: async (id: number): Promise<Payment> => {
        const response = await api.get<Payment>(`/payments/${id}`);
        return response.data;
    },

    updatePayment: async (id: number, payment: CreatePaymentRequest): Promise<Payment> => {
        const response = await api.put<Payment>(`/payments/${id}`, payment);
        return response.data;
    },

    deletePayment: async (id: number): Promise<void> => {
        await api.delete(`/payments/${id}`);
    },
}

export default paymentService;