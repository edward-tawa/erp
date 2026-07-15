import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch } from '@/store/index';
import { selectCart, selectCartLoading, selectCartError } from '@/store/features/sales/selectors/cart.selectors';
import { setCart, setLoading, setError, clearCart } from '@/store/features/sales/slices/cart.slice';
import { Cart } from '@/types/sales/cart.types';



export const useCart = () => {
    const dispatch: AppDispatch = useDispatch();
    const cart = useSelector(selectCart);
    const isLoading = useSelector(selectCartLoading);
    const error = useSelector(selectCartError);

    const handleSetCart = (cartData: Cart) => {
        dispatch(setCart(cartData));
    };

    const handleSetLoading = (loading: boolean) => {
        dispatch(setLoading(loading));
    };

    const handleSetError = (errorMessage: string | null) => {
        dispatch(setError(errorMessage));
    };

    const handleClearCart = () => {
        dispatch(clearCart());
    };

    return { cart, isLoading, error, handleSetCart, handleSetLoading, handleSetError, handleClearCart };
}
