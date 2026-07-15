import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { User } from "@/types/users/user.types";
import { LoginRequest, SignUpRequest, LoginResponse } from "@/types/auth/auth.types";
import { loginThunk, logoutThunk } from "@/store/features/auth/auth.thunks";



export interface AuthState {
    user: User | null;
    isAuthenticated: boolean;
    isLoading: boolean;
}


const initialState: AuthState = {
    user: null,
    isAuthenticated: false,
    isLoading: false,
};


const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        logout: (state) => {
            state.user = null;
            state.isAuthenticated = false;
            state.isLoading = false;
        },

        login: (state, action: PayloadAction<LoginResponse>) => {
            state.user = action.payload.user;
            state.isAuthenticated = true;
            state.isLoading = false;
        },

        setLoading: (state, action: PayloadAction<boolean>) => {
            state.isLoading = action.payload;
        },
    },

    extraReducers: (builder) => {
        builder.addCase(loginThunk.pending, (state) => {
            state.isLoading = true;
        });

        builder.addCase(loginThunk.fulfilled, (state, action: PayloadAction<LoginResponse>) => {
            state.user = action.payload.user;
            state.isAuthenticated = true;
            state.isLoading = false;
        });

        builder.addCase(loginThunk.rejected, (state) => {
            state.isLoading = false;
        });

        builder.addCase(logoutThunk.pending, (state) => {
            state.isLoading = true;
        });

        builder.addCase(logoutThunk.rejected, (state) => {
            state.isLoading = false;
        });

        builder.addCase(logoutThunk.fulfilled, (state) => {
            state.user = null;
            state.isAuthenticated = false;
            state.isLoading = false;
        });
    }
})


export const { logout, login, setLoading } = authSlice.actions;

export default authSlice.reducer;