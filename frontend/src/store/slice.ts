import {IAddToCartPayload, IChangeQuantityPayload, IInitialState} from "./types";
import {createSlice, PayloadAction} from "@reduxjs/toolkit";
import { cart } from "../data/cart.data";


const initialState: IInitialState = {
    items: cart
}


export const cartSlice = createSlice({
    name: 'cart',
    initialState,
    reducers: {
        addToCart: (state, action: PayloadAction<IAddToCartPayload>) => {
            const item = state.items.find(item => item.product.id === action.payload.product.id)
            if (!item) state.items.push({...action.payload, id: state.items.length})
        },
        removeFromCart: (state, action: PayloadAction<{id: number}>) => {
            state.items = state.items.filter(
                item => item.id !== action.payload.id
            )
        },
        changeQuantity: (state, action: PayloadAction<IChangeQuantityPayload>) => {
            const {id, type} = action.payload
           const item = state.items.find(item => item.id === id)
            if (item) type ==='plus' ? item.quantity++ : item.quantity--
        },
    }
})
