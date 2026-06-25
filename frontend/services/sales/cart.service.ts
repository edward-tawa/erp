import api from "@/services/api";
import { Cart, CreateCartRequest, CreateCartResponse, GetCartResponse } from "@/types/sales/cart.types";



const cartService = {
    createCart: async (cart: CreateCartRequest): Promise<CreateCartResponse> => {
        const response = await api.post<CreateCartResponse>("/carts", cart);
        return response.data;
    },

    getCart: async (id: number): Promise<GetCartResponse> => {
        const response = await api.get<GetCartResponse>(`/carts/${id}`);
        return response.data;
    },

    updateCart: async (id: number, cart: CreateCartRequest): Promise<GetCartResponse> => {
        const response = await api.put<GetCartResponse>(`/carts/${id}`, cart);
        return response.data;
    },

    deleteCart: async (id: number): Promise<void> => {
        await api.delete(`/carts/${id}`);
    },
}

export default cartService;