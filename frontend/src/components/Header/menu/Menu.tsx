import {FC} from 'react';

import styles from './Menu.module.scss'

const Menu: FC = () => {

    return(
        <div className={styles.menu}>
            <a href="/">
                <img src="../src/assets/logo.jpg"
                     width={200}
                     height={200}
                     alt="Apple online store"/>
            </a>

            <nav>
                <ul>
                    <li><a href="/">Main</a></li>
                    <li><a href="/">Mac</a></li>
                    <li><a href="/">iPhone</a></li>
                    <li><a href="/">Watch</a></li>
                    <li><a href="/">AirPods</a></li>
                </ul>
            </nav>
        </div>
    )

}

export default Menu