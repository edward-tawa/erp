import { User } from "@/types/users/user.types";

export interface SignUpRequest {
    firstName?: string;
    lastName?: string;
    role?: string;
    email: string;
    password: string;
    confirmPassword: string;
}


export interface SignUpResponse {
    message: string;
}


export interface LoginRequest {
    email: string;
    password: string;
}


export interface LoginResponse {
    message: string;
    user: User;
}


export interface AuthResponse {
    message: string;
}



