import { Product } from "@/types/inventory/product.types"



export interface ProductStock {
    id: number;
    product: Product;
    minStockLevel: number;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateProductStockRequest {
    product: Product;
    minStockLevel: number;
}

export interface CreateProductStockResponse {
    id: number;
}


export interface GetProductStockRequest {
    id: number;
}


export type GetProductStockResponse = ProductStock

export type UpdateProductStockRequest = Partial<ProductStock>

export type UpdateProductStockResponse = ProductStock

export interface DeleteProductStockRequest {
    id: number;
}

export interface DeleteProductStockResponse {
    message: string;
}