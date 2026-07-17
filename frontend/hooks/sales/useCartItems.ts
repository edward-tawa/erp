import { useSelector } from 'react-redux';
import { RootState } from '@/store/index';
import { selectCartItems, selectCartItemsLoading, selectCartItemsError, selectCartTotalQuantity } from '@/store/features/sales/selectors/cartItems.selectors';
import { AppDispatch } from '@/store/index';
import { setCartItems, setLoading, setError, clearCartItems } from '@/store/features/sales/slices/cartItems.slice';
import { CartItem } from '@/types/sales/cartitem.types';
import { useDispatch } from 'react-redux';


export const useCartItems = () => {
    const dispatch: AppDispatch = useDispatch();
    const cartItems = useSelector(selectCartItems);
    const isLoading = useSelector(selectCartItemsLoading);
    const error = useSelector(selectCartItemsError);
    const totalQuantity = useSelector(selectCartTotalQuantity);

    const handleSetCartItems = (cartItems: CartItem[]) => {
        dispatch(setCartItems(cartItems));
    };

    const handleSetLoading = (loading: boolean) => {
        dispatch(setLoading(loading));
    };

    const handleSetError = (errorMessage: string | null) => {
        dispatch(setError(errorMessage));
    };

    const handleClearCartItems = () => {
        dispatch(clearCartItems());
    };

    return { cartItems, isLoading, error, handleSetCartItems, handleSetLoading, handleSetError, handleClearCartItems };
}
