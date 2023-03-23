import {FC} from "react";
import Carousel from "./carousel/Carousel";
import {IProduct} from "../../../types/product.interface";
import styles from './carousel/Carousel.module.scss'

const Catalog: FC<{products: IProduct[]}> = ({products}) => {
    return(
        <div className={styles.content}>
            <Carousel products={products}/>
        </div>
    )
}

export default Catalog