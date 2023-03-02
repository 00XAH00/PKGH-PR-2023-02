import {FC, useRef, useState} from 'react';
// import { cart } from '../../../data/cart.data';
import styles from './Cart.module.scss';
import CartItem from './cart-item/CartItem';
import {Drawer, DrawerOverlay, DrawerContent, DrawerCloseButton} from "@chakra-ui/react";
import {DrawerHeader, DrawerBody, DrawerFooter, Button} from "@chakra-ui/react";
import {formatToCurrency} from "../../../utils/format-to-currency";
import {useCart} from '../../../hooks/useCart'

const Cart: FC = () => {
    const [isOpen, setIsOpen] = useState(false)
    const btnRef = useRef<HTMLButtonElement>(null)

    const {cart, total} = useCart()

    return(
        <div className={styles['wrapper-cart']}>
            <button className={styles.heading} onClick={ () => setIsOpen(!isOpen)} ref={btnRef}>
                <span className={styles.badge}>{cart.length}</span>
                <span className={styles.text}>Cart</span>
            </button>

                <Drawer
                    isOpen={isOpen}
                    placement='right'
                    onClose={() => setIsOpen(false)}
                >
                    <DrawerOverlay />
                    <DrawerContent>
                        <DrawerCloseButton />
                        <DrawerHeader className={styles.headerCart}>Cart</DrawerHeader>

                        <DrawerBody>
                            <div className={styles.cart}>
                                {cart.length ? cart.map(item => (
                                    <CartItem item={item} key={item.id}/>
                                )): <div>The cart is empty</div>}
                            </div>
                        </DrawerBody>

                        <DrawerFooter
                            justifyContent='space-between'
                            borderTopColor={'gray.300'}
                            borderTopWidth={1}
                        >
                                <div className={styles.footer}>
                                    <div>Total price:</div>
                                    <div>{formatToCurrency(total)}</div>
                                </div>
                            <Button colorScheme='pink'>Checkout</Button>
                        </DrawerFooter>
                    </DrawerContent>
                </Drawer>
        </div>
    )
}

export default Cart