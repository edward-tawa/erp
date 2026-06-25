import { Product } from "@/types/inventory/product.types";
import { SalesOrderItem } from "@/types/sales/salesorderitem.types";
import { Cart } from "@/types/sales/cart.types";

export interface CartItem {
    id: number;
    product: Product;
    cart: Cart;
    salesOrderItem: SalesOrderItem;
    quantity: number;
    unitPrice: number;
    createdAt: string;
    updatedAt?: string;
}

export interface CreateCartItemRequest {
    product: Product;
    cart: Cart;
    salesOrderItem: SalesOrderItem;
    quantity: number;
    unitPrice: number;
}

export interface CreateCartItemResponse {
    id: number;
}

export interface GetCartItemRequest {
    id: number;
}

export type GetCartItemResponse = CartItem;

export type UpdateCartItemRequest = Partial<CartItem>;

export type UpdateCartItemResponse = CartItem;

export interface DeleteCartItemRequest {
    id: number;
}

export interface DeleteCartItemResponse {
    message: string;
}