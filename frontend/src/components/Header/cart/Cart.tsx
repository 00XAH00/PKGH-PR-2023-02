import {FC, useRef, useState} from 'react';
// import { cart } from '../../../data/cart.data';
import styles from './Cart.module.scss';
import CartItem from './cart-item/CartItem';
import {Drawer, DrawerOverlay, DrawerContent, DrawerCloseButton} from "@chakra-ui/react";
import {DrawerHeader, DrawerBody, DrawerFooter, Button} from "@chakra-ui/react";
import {useTypedSelector} from "../../../hooks/useTypedSelector";

const Cart: FC = () => {
    const [isOpen, setIsOpen] = useState(false)
    const btnRef = useRef<HTMLButtonElement>(null)

    const cart = useTypedSelector(state => (state.cart.items))

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
                                {cart.map(item => (
                                    <CartItem item={item} key={item.id}/>
                                ))}
                            </div>
                        </DrawerBody>

                        <DrawerFooter
                            justifyContent='space-between'
                            borderTopColor={'gray.300'}
                            borderTopWidth={1}
                        >
                                <div className={styles.footer}>
                                    <div>Total price:</div>
                                    <div>$2000</div>
                                </div>
                            <Button colorScheme='pink'>Checkout</Button>
                        </DrawerFooter>
                    </DrawerContent>
                </Drawer>
        </div>
    )
}

export default Cart