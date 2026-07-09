export interface User {
    id: string;
    firstName: string;
    lastName: string;
    isActive: boolean;
    email: string;
    role: string;
    createdAt: string;
    updatedAt?: string | null;
}


export interface CreateUserRequest {
    firstName: string;
    lastName: string;
    email: string;
    password: string;
    confirmPassword: string;
    role: string;
}



export interface GetUserRequest {
    id: number;
}


export type GetUserResponse = User;



export type UpdateUserRequest =
    Partial<Omit<CreateUserRequest, "confirmPassword">>;



export type UpdateUserResponse = User;


export interface DeleteUserRequest {
    id: number;
}


export interface DeleteUserResponse {
    message: string;
}


