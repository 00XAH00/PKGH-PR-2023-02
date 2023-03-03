import {FC, useState} from "react";
import CarouselItem from "./carousel-item/CarouselItem";
import {IProduct} from "../../../../types/product.interface";
import styles from './Carousel.module.scss'

const Carousel: FC<{products: IProduct[]}> = ({products}) => {
    const [selectedItemIndex, setSelectedItemIndex] = useState(1)


    return(
        <section className={styles.carousel}>
            {products.map((product, index) =>
                <CarouselItem
                    product={product}
                    key={product.id}
                    isActive={index === selectedItemIndex}
                    selectItem = {() => setSelectedItemIndex(index)}
                />
            )}
        </section>
    )
}

export default Carousel