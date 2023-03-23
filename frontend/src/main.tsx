import React from 'react'
import ReactDOM from 'react-dom/client'
import Home from "./pages/Home";
import './index.css'
import { ChakraProvider } from '@chakra-ui/react'
import {Provider} from "react-redux";
import {persistor, store} from "./store/store";
import { PersistGate } from 'redux-persist/integration/react'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
    <Provider store={store}>
        <PersistGate loading={null} persistor={persistor}>
            <ChakraProvider>
                <Home/>
            </ChakraProvider>
        </PersistGate>
    </Provider>
)
