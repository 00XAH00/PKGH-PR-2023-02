import {FC} from "react";
import {IProduct} from "../../../../../types/product.interface";
import styles from '../Carousel.module.scss'
import cn from "clsx";
// import {useActions} from "../../../../../hooks/useActions";
import CarouselButton from "./CarouselButton";

const CarouselItem: FC<{product: IProduct}> = ({product}) => {
    const isActive = product.id === 2

    // const {addToCart} = useActions()

    return(
        <div className={cn(styles.item, {
            [styles.active]: isActive
        })}>

            <div>
                <img
                    className={styles.image}
                    alt={product.name}
                    src={product.images[0]}

                />

                <div className={styles.heading}>
                    {product.name}
                </div>

                {isActive ?
                        <div>
                            {/*  variations  */}
                            <CarouselButton product={product}/>
                        </div>
                    : (
                    <div className={styles.description}>{product.description}</div>
                )}
            </div>
        </div>
    )
}

export default CarouselItem