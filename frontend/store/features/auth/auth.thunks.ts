import { createAsyncThunk } from "@reduxjs/toolkit";
import { LoginRequest, SignUpRequest, LoginResponse } from "@/types/auth/auth.types";
import { authService } from "@/services/auth/auth.service";


export const loginThunk = createAsyncThunk(
    'auth/login',
    async (loginRequest: LoginRequest, thunkAPI) => {
        try {
            const response: LoginResponse = await authService.login(loginRequest);
            return response;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
)


export const logoutThunk = createAsyncThunk(
    'auth/logout',
    async (_, thunkAPI) => {
        try {
            await authService.logout();
            return;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data || error.message);
        }
    }
)