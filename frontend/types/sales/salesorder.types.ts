import { Customer } from "@/types/sales/customer.types";

type Status =
    | "PENDING"
    | "CONFIRMED"
    | "SHIPPED"
    | "DELIVERED"
    | "CANCELLED";



export interface SalesOrder {
    id: string;
    customer: Customer;
    orderNumber: string;
    status: Status;
    totalAmount: number;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateSalesOrderRequest {
    customer: Customer;
    orderNumber: string;
    status: Status;
    totalAmount: number;
}

export interface CreateSalesOrderResponse {
    id: number;
}


export interface GetSalesOrderRequest {
    id: number;
}



export type GetSalesOrderResponse = SalesOrder;

export type UpdateSalesOrderRequest = Partial<SalesOrder>;

export type UpdateSalesOrderResponse = SalesOrder;

export interface DeleteSalesOrderRequest {
    id: string;
}

export interface DeleteSalesOrderResponse {
    message: string;
}


