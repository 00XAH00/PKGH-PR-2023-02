import {FC} from "react";
import styles from '../Cart.module.scss'
import { ICartItem } from "../../../../types/cart.interface";
import CartActions from "./cart-actions/CartActions";


const CartItem: FC<{item: ICartItem}> = ({item}) => {
    return(
        <div className={styles.item}>
            <img
                className={styles.cartImg}
                src={item.product.images[0]}
                width={100}
                height={100}
                alt={item.product.name}
            />
            <div>
                <p className={styles.name}>{item.product.name}</p>
                <p className={styles.price}>
                    {new Intl.NumberFormat('en-US',{
                        style: 'currency', currency: 'USD'
                    }).format(item.product.price)}
                </p>
                <CartActions/>
            </div>
        </div>
    )
}

export default CartItem