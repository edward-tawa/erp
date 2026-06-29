import { Product } from "@/types/inventory/product.types";
import { SalesOrderItem } from "@/types/sales/salesorderitem.types";
import { Receipt } from "@/types/sales/receipt.types";


export interface ReceiptItem {
    id: number;
    product: Product;
    salesOrderItem: SalesOrderItem;
    receipt: Receipt;
    quantity: number;
    unitPrice: number;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateReceiptItemRequest {
    product: Product;
    salesOrderItem: SalesOrderItem;
    receipt: Receipt;
    quantity: number;
    unitPrice: number;
}

export interface CreateReceiptItemResponse {
    id: number;
}

export interface GetReceiptItemRequest {
    id: number;
}

export type GetReceiptItemResponse = ReceiptItem;

export type UpdateReceiptItemRequest = Partial<ReceiptItem>;

export type UpdateReceiptItemResponse = ReceiptItem;

export interface DeleteReceiptItemRequest {
    id: number;
}

export interface DeleteReceiptItemResponse {
    message: string;
}