import api from "@/services/api";
import { CartItem, CreateCartItemRequest, CreateCartItemResponse, GetCartItemResponse } from "@/types/sales/cartitem.types";

const cartItemService = {
    createCartItem: async (cartItem: CreateCartItemRequest): Promise<CreateCartItemResponse> => {
        const response = await api.post<CreateCartItemResponse>("/cart-items", cartItem);
        return response.data;
    },

    getCartItem: async (id: number): Promise<GetCartItemResponse> => {
        const response = await api.get<GetCartItemResponse>(`/cart-items/${id}`);
        return response.data;
    },

    updateCartItem: async (id: number, cartItem: CreateCartItemRequest): Promise<GetCartItemResponse> => {
        const response = await api.put<GetCartItemResponse>(`/cart-items/${id}`, cartItem);
        return response.data;
    },

    deleteCartItem: async (id: number): Promise<void> => {
        await api.delete(`/cart-items/${id}`);
    },
}

export default cartItemService;