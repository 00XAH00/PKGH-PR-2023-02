import {cartSlice} from "../store/slice";
import {useDispatch} from "react-redux";
import {bindActionCreators} from 'redux'
import {useMemo} from "react";


const rootAction = {
    ...cartSlice.actions
}

export const useActions = () => {
    const dispatch = useDispatch()

    return useMemo(()=> bindActionCreators(rootAction, dispatch), [dispatch])
}