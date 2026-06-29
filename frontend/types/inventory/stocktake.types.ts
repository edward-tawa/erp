import { User } from "@/types/users/user.types";
import { Product } from "@/types/inventory/product.types";

export type Status = "ONGOING" | "COMPLETED" | "CANCELLED";

export interface Stocktake {
    id: number;
    referenceNumber: string;
    product: Product;
    takenBy: User;
    dateTaken: string;
    status: Status;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateStocktakeRequest {
    referenceNumber: string;
    product: Product;
    takenBy: User;
    dateTaken: string;
    status: Status;
}

export interface CreateStocktakeResponse {
    id: number;
}

export interface GetStocktakeRequest {
    id: number;
}

export type GetStocktakeResponse = Stocktake;

export type UpdateStocktakeRequest = Partial<Stocktake>;

export type UpdateStocktakeResponse = Stocktake;

export interface DeleteStocktakeRequest {
    id: number;
}

export interface DeleteStocktakeResponse {
    message: string;
}
