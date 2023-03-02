import {FC} from "react";
import {IProduct} from "../../../../../types/product.interface";
import styles from './Carousel.module.scss'

const CarouselItem: FC<{product: IProduct}> = ({product}) => {
    return(
        <div>
            <img alt={product.name} src={product.images[0]} width={200} height={200}/>

            <div className={styles.heading}></div>


        </div>
    )
}

export default CarouselItem