import api from "@/services/api";
import { LoginRequest, LoginResponse, SignUpRequest } from "@/types/auth/auth.types";


export const authService = {
    signUp: async (signUpData: SignUpRequest) => {
        const response = await api.post<SignUpRequest>("/auth/signup", signUpData);
        return response.data;
    },

    login: async (loginData: LoginRequest): Promise<LoginResponse> => {
        const response = await api.post<LoginResponse>("/auth/login", loginData);
        return response.data;
    },

    logout: async () => {
        const response = await api.post("/auth/logout");
        return response.data;
    },
};