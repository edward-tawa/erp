import { RootState } from "@/store";

export const selectUser = (state: RootState) => state.auth.user;

export const selectIsAuthenticated = (state: RootState) =>
    state.auth.isAuthenticated;

export const selectIsLoading = (state: RootState) =>
    state.auth.isLoading;