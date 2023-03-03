import {FC} from "react";
import styles from "../Carousel.module.scss";
import {useActions} from "../../../../../hooks/useActions";
import {IProduct} from "../../../../../types/product.interface";

const CarouselButton: FC<{product: IProduct}> = ({product}) => {
    const {addToCart} = useActions()

    return(
        <div className='text-center'>
            <button
                onClick={() =>
                    addToCart({
                    product,
                    quantity: 1
                })
                }
                className={styles.addBtn}
            >
                Add to Cart
            </button>
        </div>
    )
}

export default CarouselButton