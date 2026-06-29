import { Customer } from "@/types/sales/customer.types";
import { Cart } from "@/types/sales/cart.types";



export interface Checkout {
    id: number;
    customer: Customer;
    cart: Cart;
    notes?: string;
}



export interface CreateCheckoutRequest {
    customer: Customer;
    cart: Cart;
    notes?: string;
}


export interface CreateCheckoutResponse {
    id: number;
}

export interface GetCheckoutRequest {
    id: number;
}

export type GetCheckoutResponse = Checkout;

export type UpdateCheckoutRequest = Partial<Checkout>;

export type UpdateCheckoutResponse = Checkout;

export interface DeleteCheckoutRequest {
    id: number;
}

export interface DeleteCheckoutResponse {
    message: string;
}