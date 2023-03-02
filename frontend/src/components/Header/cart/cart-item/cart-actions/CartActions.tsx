import {FC} from "react";
import {Button, HStack, useNumberInput} from "@chakra-ui/react";
import {Input} from "@chakra-ui/react";
import {AddIcon, MinusIcon} from "@chakra-ui/icons";
import {useActions} from "../../../../../hooks/useActions";

import {ICartItem} from "../../../../../types/cart.interface";

const CartActions: FC<{item: ICartItem}> = ({item}) => {
    const { getInputProps, getIncrementButtonProps, getDecrementButtonProps } =
        useNumberInput({
            step: 1,
            defaultValue: 1,
            min: 1
        })

    const inc = getIncrementButtonProps()
    const dec = getDecrementButtonProps()
    const input = getInputProps()

    const {removeFromCart, changeQuantity} = useActions()

    return(
        <div>
            <HStack>
                <Button {...dec} boxSize={10} onClick={() => changeQuantity({id: item.id, type: 'minus'})}>
                    <MinusIcon width='8px'/>
                </Button>

                <Input {...input}
                       focusBorderColor='pink.400'
                       textAlign='center'
                       height='40px'
                       readOnly
                       _hover={{cursor: 'default'}}
                />

                <Button {...inc} boxSize={10} onClick={() => changeQuantity({id: item.id, type: 'plus'})}>
                    <AddIcon width='8px'/>
                </Button>
            </HStack>

            <Button
                variant='unstyled'
                color='#f23c3d'
                marginTop={2}
                size='md'
                opacity={0.8}
                onClick={() => removeFromCart({id: item.id})}
            >
                Delete
            </Button>
        </div>

    )
}

export default CartActions