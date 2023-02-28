import {FC, useState} from 'react';
import { cart } from '../../../data/cart.data';
import styles from './Cart.module.scss';
import CartItem from './cart-item/CartItem';

const Cart: FC = () => {
    const [isOpen, setIsOpen] = useState(false)
    return(
        <div className={styles['wrapper-cart']}>
            <button className={styles.heading} onClick={ () => setIsOpen(!isOpen)}>
                <span className={styles.badge}>B</span>
                <span className={styles.text}>Cart</span>
            </button>
            {isOpen &&(
            <div className={styles.cart}>
                {cart.map(item => (
                    <CartItem item={item} key={item.id}/>
                ))}
            </div>
            )}
        </div>
    )
}

export default Cart