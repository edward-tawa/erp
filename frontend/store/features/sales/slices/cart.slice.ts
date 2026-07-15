import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Cart } from '@/types/sales/cart.types';




export interface CartState {
    cart: Cart | null;
    isLoading: boolean;
    error: string | null;
}

const initialState: CartState = {
    cart: null,
    isLoading: false,
    error: null,
}



const cartSlice = createSlice({
    name: 'cartSlice',
    initialState,
    reducers: {
        setCart: (state, action: PayloadAction<Cart>) => {
            state.cart = action.payload;
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

        clearCart: (state) => {
            state.cart = null;
            state.isLoading = false;
            state.error = null;
        },

    }
})




export const { setCart, setLoading, setError, clearCart } = cartSlice.actions;

export default cartSlice.reducer;