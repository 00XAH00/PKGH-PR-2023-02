import {FC} from 'react';
import styles from './Header.module.scss'
import Menu from "./menu/Menu";
import Search from "./search/Search";
import Cart from "./cart/Cart";



const Header: FC = () => {

    return(
        <header className={styles.header}>
            <Menu/>
            <Search/>
            <Cart/>
        </header>
    )
}
export default Header