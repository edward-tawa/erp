import { Receipt } from "@/types/sales/receipt.types";
import { User } from "@/types/users/user.types";


export interface Payment {
    id: number;
    receipt: Receipt;
    user?: User;
    totalAmount: number;
    paymentType: string;
    denomination: string;
    createdAt: string;
    updatedAt?: string;
}



export interface CreatePaymentRequest {
    receipt: Receipt;
    user?: User;
    totalAmount: number;
    paymentType: string;
    denomination: string;
}

export interface CreatePaymentResponse {
    id: number;
}

export interface GetPaymentRequest {
    id: number;
}

export type GetPaymentResponse = Payment;

export type UpdatePaymentRequest = Partial<Payment>;

export type UpdatePaymentResponse = Payment;

export interface DeletePaymentRequest {
    id: number;
}

export interface DeletePaymentResponse {
    message: string;
}