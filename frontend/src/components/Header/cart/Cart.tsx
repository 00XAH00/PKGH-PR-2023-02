import {FC} from 'react';
import { cart } from '../../../data/cart.data';
import styles from './cart-item/Cart.module.scss';
import CartItem from './cart-item/CartItem';

const Cart: FC = () => {

    return(
        <div className={styles['wrapper-cart']}>
            <button className={styles.heading}>
                <span className={styles.badge}>My </span>
                <span className={styles.text}>Cart</span>
            </button>

            <div className={styles.cart}>
                {cart.map(item => (
                    <CartItem item={item} key={item.id}/>
                ))}
            </div>
        </div>
    )
}

export default Cart