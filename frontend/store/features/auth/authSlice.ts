import { createSlice } from "@reduxjs/toolkit";
import { AuthState } from "@/types/auth/auth.types";


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
        },

        login: (state, action) => {
            state.user = action.payload;
            state.isAuthenticated = true;
        },

        setLoading: (state, action) => {
            state.isLoading = action.payload;
        },
    },
})


export const { logout, login, setLoading } = authSlice.actions;

export default authSlice.reducer;