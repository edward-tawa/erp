import api from "@/services/api";
import { Checkout, CreateCheckoutRequest, GetCheckoutResponse } from "@/types/sales/checkout.types";


const checkoutService = {
    createCheckout: async (checkout: CreateCheckoutRequest): Promise<CreateCheckoutRequest> => {
        const response = await api.post<CreateCheckoutRequest>("/checkouts", checkout);
        return response.data;
    },

    getCheckout: async (id: number): Promise<GetCheckoutResponse> => {
        const response = await api.get<GetCheckoutResponse>(`/checkouts/${id}`);
        return response.data;
    },

    updateCheckout: async (id: number, checkout: CreateCheckoutRequest): Promise<CreateCheckoutRequest> => {
        const response = await api.put<CreateCheckoutRequest>(`/checkouts/${id}`, checkout);
        return response.data;
    },

    deleteCheckout: async (id: number): Promise<void> => {
        const response = await api.delete(`/checkouts/${id}`);
        return response.data;
    },


}

export default checkoutService;