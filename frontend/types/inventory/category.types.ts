export interface Category {
    id: number;
    name: string;
    description: string;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateCategoryRequest {
    name: string;
    description: string;
}

export interface CreateCategoryResponse {
    id: number;
    name: string;
    description: string;
    createdAt: string;
    updatedAt?: string;
}

export interface GetCategoryRequest {
    name: string;
}


export type GetCategoryResponse = Category;


export type UpdateCategoryRequest = Partial<Category>;


export type UpdateCategoryResponse = Category;


export interface DeleteCategoryRequest {
    id: number;
}


export interface DeleteCategoryResponse {
    message: string;
}