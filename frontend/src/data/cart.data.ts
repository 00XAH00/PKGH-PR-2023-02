import {ICartItem} from "../types/cart.interface";
import {products} from "./product.data";

export const cart:ICartItem[] = [
    {
        id: 1,
        quantity: 1,
        product: products[0]
    },
    {
        id: 2,
        quantity: 2,
        product: products[1]
    }
]