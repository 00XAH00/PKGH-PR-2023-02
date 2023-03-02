import {cartSlice} from "../store/slice";
import {useDispatch} from "react-redux";
import {bindActionCreators} from 'redux'


const rootAction = {
    ...cartSlice.actions
}

export const useActions = () => {
    const dispatch = useDispatch()

    return bindActionCreators(rootAction, dispatch)
}