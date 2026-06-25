export interface User {
    id: string;
    firstName: string;
    lastName: string;
    isActive: boolean;
    email: string;
    role: string;
    createdAt: string;
    updatedAt?: string;
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
    id: string;
}



export type GetUserResponse = User;




export type UpdateUserRequest =
    Partial<Omit<CreateUserRequest, "confirmPassword">>;



export type UpdateUserResponse = User;


export interface DeleteUserRequest {
    id: string;
}


export interface DeleteUserResponse {
    message: string;
}


