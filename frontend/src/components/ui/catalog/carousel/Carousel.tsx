import {FC} from "react";
import CarouselItem from "./carousel-item/CarouselItem";
import {IProduct} from "../../../../types/product.interface";
import styles from './Carousel.module.scss'

const Carousel: FC<{products: IProduct[]}> = ({products}) => {
    return(
        <section className={styles.carousel}>
            {products.map(product => <CarouselItem product={product} key={product.id}/>)}
        </section>
    )
}

export default Carousel