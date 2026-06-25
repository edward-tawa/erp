import { User } from "@/types/users/user.types";


export interface Cart {
    id: number;
    user: User;
    referenceNumber: string;
    totalAmount: number;
    createdAt: string;
    updatedAt?: string;
}



export interface CreateCartRequest {
    user?: User;
    referenceNumber?: string;
    totalAmount?: number;
}


export interface CreateCartResponse {
    id: number;
}

export interface GetCartRequest {
    id: number;
}

export type GetCartResponse = Cart;

export type UpdateCartRequest = Partial<Cart>;

export type UpdateCartResponse = Cart;

export interface DeleteCartRequest {
    id: number;
}

export interface DeleteCartResponse {
    message: string;
}



