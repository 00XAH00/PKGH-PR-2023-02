import {combineReducers, configureStore} from "@reduxjs/toolkit";
import {cartSlice} from './slice'
import { persistStore, persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage'
import {FLUSH, PAUSE, PERSIST, PURGE, REGISTER, REHYDRATE} from "redux-persist/es/constants"; // defaults to localStorage for web

//persistConfig это настройка самого redux-persist
const persistConfig = {
    key: 'apple-devices',
    storage,
    whitelist: ['cart']
}

const rootReducer = combineReducers({
    cart: cartSlice.reducer
})

const persistedReducer = persistReducer(persistConfig, rootReducer)

export const store = configureStore({
    reducer: persistedReducer,
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            serializableCheck:{
                ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
            },
        }),
})

export const persistor = persistStore(store)

export type TypeRootState = ReturnType<typeof rootReducer>