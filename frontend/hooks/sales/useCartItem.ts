import { AppDispatch, RootState } from "@/store/index";
import { useDispatch, useSelector } from "react-redux";
import { selectCartItem, selectCartItemLoading, selectCartItemError, selectCartItemByProductName, selectCartItemById } from "@/store/features/sales/selectors/cartItem.selectors";
import { CartItem } from "@/types/sales/cartitem.types";
import { setCartItem, setLoading, setError, clearCartItem } from "@/store/features/sales/slices/cartItem.slice";


export const useCartItem = (productName?: string, id?: number) => {
    const dispatch: AppDispatch = useDispatch();
    const cartItem = useSelector((state: RootState) => {
        if (id) return selectCartItemById(state, id);
        if (productName) return selectCartItemByProductName(state, productName);
        return selectCartItem(state);
    });
    const isLoading = useSelector(selectCartItemLoading);
    const error = useSelector(selectCartItemError);

    const handleSetCartItem = (cartItemData: CartItem) => {
        dispatch(setCartItem(cartItemData));
    };

    const handleSetLoading = (loading: boolean) => {
        dispatch(setLoading(loading));
    };

    const handleSetError = (errorMessage: string | null) => {
        dispatch(setError(errorMessage));
    };

    const handleClearCartItem = () => {
        dispatch(clearCartItem());
    };

    return { cartItem, isLoading, error, handleSetCartItem, handleSetLoading, handleSetError, handleClearCartItem };
}