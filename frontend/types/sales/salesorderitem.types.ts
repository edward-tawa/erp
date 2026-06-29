import { SalesOrder } from "@/types/sales/salesorder.types";
import { Product } from "@/types/inventory/product.types"


export interface SalesOrderItem {
    salesOrder: SalesOrder;
    product: Product;
    quantity: number;
    unitPrice: number;
    createdAt: string;
    updatedAt?: string;
}



export interface CreateSalesOrderItemRequest {
    salesOrder: SalesOrder;
    product: Product;
    quantity: number;
    unitPrice: number;
}


export interface CreateSalesOrderItemResponse {
    id: number;
}


export interface GetSalesOrderItemRequest {
    id: number;
}


export type GetSalesOrderItemResponse = SalesOrderItem


export type UpdateSalesOrderItemRequest = Partial<SalesOrderItem>


export type UpdateSalesOrderItemResponse = SalesOrderItem


export interface DeleteSalesOrderItemRequest {
    id: number;
}

export interface DeleteSalesOrderItemResponse {
    id: number;
}