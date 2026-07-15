import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { CartItem } from '@/types/sales/cartitem.types';


export interface CartItemState {
    cartItem: CartItem | null;
    isLoading: boolean;
    error: string | null;
}



const initialState: CartItemState = {
    cartItem: null,
    isLoading: false,
    error: null,
}

const cartItemSlice = createSlice({
    name: 'cartItemSlice',
    initialState,
    reducers: {
        setCartItem: (state, action: PayloadAction<CartItem>) => {
            state.cartItem = action.payload;
            state.isLoading = false;
            state.error = null;
        },

        setLoading: (state, action: PayloadAction<boolean>) => {
            state.isLoading = action.payload;
        },

        setError: (state, action: PayloadAction<string | null>) => {
            state.error = action.payload;
            state.isLoading = false;
        },

        clearCartItem: (state) => {
            state.cartItem = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})


export const { setCartItem, setLoading, setError, clearCartItem } = cartItemSlice.actions;

export default cartItemSlice.reducer;