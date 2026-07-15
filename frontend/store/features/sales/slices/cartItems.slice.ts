import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { CartItem } from "@/types/sales/cartitem.types";


export interface CartItemsState {
    cartItems: CartItem[] | null;
    isLoading: boolean;
    error: string | null;
}


const initialState: CartItemsState = {
    cartItems: null,
    isLoading: false,
    error: null,
}

const cartItemsSlice = createSlice({
    name: 'cartItemsSlice',
    initialState,
    reducers: {
        setCartItems: (state, action: PayloadAction<CartItem[]>) => {
            state.cartItems = action.payload;
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

        clearCartItems: (state) => {
            state.cartItems = null;
            state.isLoading = false;
            state.error = null;
        },
    }
})


export const { setCartItems, setLoading, setError, clearCartItems } = cartItemsSlice.actions;

export default cartItemsSlice.reducer;