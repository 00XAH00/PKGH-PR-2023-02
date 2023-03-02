import React from 'react'
import ReactDOM from 'react-dom/client'
import Home from "./pages/Home";
import './index.css'
import { ChakraProvider } from '@chakra-ui/react'
import {Provider} from "react-redux";
import {store} from "./store/store";

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
    <Provider store={store}>
        <ChakraProvider>
            <Home/>
        </ChakraProvider>
    </Provider>
)
