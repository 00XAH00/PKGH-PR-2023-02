import {FC} from 'react';
// import styles from './Home.module.scss'
import Header from "../components/Header/Header";
import Catalog from "../components/ui/catalog/Catalog";
import { products } from '../data/product.data';

const Home: FC = () => {
    return(
        <div>
            <Header/>
            <Catalog products={products}/>
        </div>
    )
}
export default Home