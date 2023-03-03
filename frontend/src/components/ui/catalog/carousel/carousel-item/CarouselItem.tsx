import {FC} from "react";
import {IProduct} from "../../../../../types/product.interface";
import styles from './Carousel.module.scss'
import cn from "clsx";

const isActive = false//временная заглушка

const CarouselItem: FC<{product: IProduct}> = ({product}) => {
    return(
        <div className={cn(styles.item, {
            [styles.active]: isActive
        })}>

            <img className={styles.image} alt={product.name} src={product.images[0]} width={200} height={200}/>

            <div className={styles.heading}>
                {product.name}
            </div>

            <div className={styles.description}>
                {product.description}
            </div>

        </div>
    )
}

export default CarouselItem