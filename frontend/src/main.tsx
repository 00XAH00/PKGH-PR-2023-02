import React from 'react'
import ReactDOM from 'react-dom/client'
// import App from './App'
import Home from "./pages/Home";
import './index.css'
import { ChakraProvider } from '@chakra-ui/react'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
    <ChakraProvider>
        <Home/>
    </ChakraProvider>
)
