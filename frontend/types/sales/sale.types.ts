import { User } from "@/types/users/user.types";
import { SalesOrder } from "@/types/sales/salesorder.types";
import { Receipt } from "@/types/sales/receipt.types";



export interface Sale {
    id: number;
    saleReferenceNumber: string;
    user: User;
    salesOrder: SalesOrder;
    receipt: Receipt;
    notes: string;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateSaleRequest {
    saleReferenceNumber?: string;
    user?: User;
    salesOrder: SalesOrder;
    receipt: Receipt;
    notes?: string;
}


export interface CreateSaleResponse {
    id: number;
}

export interface GetSaleRequest {
    id: number;
}

export type GetSaleResponse = Sale;

export type UpdateSaleRequest = Partial<Sale>;

export type UpdateSaleResponse = Sale;

export interface DeleteSaleRequest {
    id: number;
}

export interface DeleteSaleResponse {
    message: string;
}