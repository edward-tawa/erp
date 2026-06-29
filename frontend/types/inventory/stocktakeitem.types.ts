import { Stocktake } from "@/types/inventory/stocktake.types";
import { Product } from "@/types/inventory/product.types";

export interface StocktakeItem {
    id: number;
    stocktake: Stocktake;
    product: Product;
    quantity: number;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateStocktakeItemRequest {
    stocktake: Stocktake;
    product: Product;
    quantity: number;
}


export interface CreateStocktakeItemResponse {
    id: number;
}


export interface GetStocktakeItemRequest {
    id: number;
}


export type GetStocktakeItemResponse = StocktakeItem;


export type UpdateStocktakeItemRequest = Partial<StocktakeItem>;


export type UpdateStocktakeItemResponse = StocktakeItem;


export interface DeleteStocktakeItemRequest {
    id: number;
}


export interface DeleteStocktakeItemResponse {
    message: string;
}