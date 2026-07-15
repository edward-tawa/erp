import api from "@/services/api";
import { User, CreateUserRequest, CreateUserResponse, UpdateUserRequest, UpdateUserResponse, DeleteUserResponse } from "@/types/users/user.types";

const userService = {
    createUser: async (user: CreateUserRequest): Promise<CreateUserResponse> => {
        const response = await api.post<CreateUserResponse>("/users", user);
        return response.data;
    },

    getUser: async (id: number): Promise<User> => {
        const response = await api.get<User>(`/users/${id}`);
        return response.data;
    },

    updateUser: async (id: number, user: UpdateUserRequest): Promise<UpdateUserResponse> => {
        const response = await api.put<UpdateUserResponse>(`/users/${id}`, user);
        return response.data;
    },

    deleteUser: async (id: number): Promise<DeleteUserResponse> => {
        const response = await api.delete<DeleteUserResponse>(`/users/${id}`);
        return response.data;
    },
}

export default userService;