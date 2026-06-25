import { User } from "@/types/users/user.types";
import { SalesOrder } from "@/types/sales/salesorder.types";


export interface Receipt {
    id: string;
    receiptReference?: string;
    salesOrder: SalesOrder;
    user: User;
    totalAmount: number;
    notes: string;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateReceiptRequest {
    receiptReference?: string;
    salesOrder: SalesOrder;
    user: User;
    totalAmount: number;
    notes: string;
}



export interface CreateReceiptResponse {
    id: number;
}

export interface GetReceiptRequest {
    id: string;
}


export type GetReceiptResponse = Receipt;

export type UpdateReceiptRequest = Partial<Receipt>;

export type UpdateReceiptResponse = Receipt;

export interface DeleteReceiptRequest {
    id: string;
}

export interface DeleteReceiptResponse {
    message: string;
}