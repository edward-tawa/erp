import { useDispatch, useSelector } from "react-redux";
import { AppDispatch } from "@/store/index";
import { selectUser, selectIsAuthenticated, selectIsLoading } from "@/store/features/auth/auth.selectors";
import { logout, login, setLoading } from "@/store/features/auth/auth.slice";
import { LoginRequest } from "@/types/auth/auth.types";
import { loginThunk, logoutThunk } from "@/store/features/auth/auth.thunks";

export const useAuth = () => {
    const dispatch: AppDispatch = useDispatch();
    const user = useSelector(selectUser);
    const isAuthenticated = useSelector(selectIsAuthenticated);
    const isLoading = useSelector(selectIsLoading);

    const handleLogin = async (userData: LoginRequest) => {
        try {
            dispatch(setLoading(true));
            await dispatch(loginThunk(userData)).unwrap();
        }
        catch (error) {
            console.error("Error during login:", error);
        }
        finally {
            dispatch(setLoading(false));
        }
    };


    const handleLogout = () => {
        dispatch(logout());
    };

    const handleSetLoading = (loading: boolean) => {
        dispatch(setLoading(loading));
    };

    return { user, isAuthenticated, isLoading, dispatch, handleLogin, handleLogout, handleSetLoading };
}