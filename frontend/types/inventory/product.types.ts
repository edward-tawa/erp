import { Category } from "@/types/inventory/category.types"



export interface Product {
    id: number;
    name: string;
    category: Category;
    sku: string;
    price: number;
    image: string;
    createdAt: string;
    UpdatedAt: string;
}

export interface CreateProductRequest {
    name: string;
    category: Category;
    price: number;
}

export interface CreateProductResponse {
    id: number;
    name: string;
    category: Category;
    sku: string;
    price: number;
    image: string;
    createdAt: string;
    UpdatedAt: string;
}


export interface GetProductRequest {
    id: number;
}


export type GetProductResponse = Product


export type UpdateProductRequest = Partial<Product>

export type UpdateProductResponse = Product


export interface DeleteProductRequest {
    id: number;
}


export interface DeleteProductResponse {
    message: string;
}