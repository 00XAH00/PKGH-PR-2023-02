import {FC} from 'react';
// import styles from './Home.module.scss'
import Header from "../components/Header/Header";
import Catalog from "../components/ui/catalog/Catalog";

const Home: FC = () => {
    return(
        <div>
            <Header/>
            <Catalog/>
        </div>
    )
}
export default Home