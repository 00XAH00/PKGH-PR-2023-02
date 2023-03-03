import {FC} from "react";
import {IProduct} from "../../../../../types/product.interface";
import styles from '../Carousel.module.scss'
import cn from "clsx";

const CarouselItem: FC<{product: IProduct}> = ({product}) => {
    const isActive = product.id === 2
    return(
        <div className={cn(styles.item, {
            [styles.active]: isActive
        })}>

            <img
                className={styles.image}
                alt={product.name}
                src={product.images[0]}

            />

            <div className={styles.heading}>
                {product.name}
            </div>

            {!isActive && (
                <div className={styles.description}>{product.description}</div>
            )}

        </div>
    )
}

export default CarouselItem