import {ICartItem} from "../types/cart.interface";

export interface IInitialState{
    items: ICartItem[]
}

export interface IAddToCartPayload extends Omit<ICartItem, 'id'>{}

//interface для changeQuantity в slice
export interface IChangeQuantityPayload extends Pick<ICartItem, 'id'>{
    type: 'minus' | 'plus'
}