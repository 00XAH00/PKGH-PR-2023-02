import {FC} from "react";
import {IProduct} from "../../../../../types/product.interface";
import styles from '../Carousel.module.scss'
import cn from "clsx";
import CarouselButton from "./CarouselButton";

interface ICarouselItem{
    isActive: boolean
    selectItem: () => void
    product: IProduct
}

const CarouselItem: FC<ICarouselItem> = ({product,isActive, selectItem}) => {
    // const isActive = product.id === 2


    return(
        <button className={cn(styles.item, {
            [styles.active]: isActive
        })}
             onClick={selectItem}
        >

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
                            <CarouselButton product={product}/>
                        </div>
                    : (
                    <div className={styles.description}>{product.description}</div>
                )}
            </div>
        </button>
    )
}

export default CarouselItem