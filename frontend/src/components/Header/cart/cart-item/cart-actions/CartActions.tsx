import {FC} from "react";
import {Button, HStack, useNumberInput} from "@chakra-ui/react";
import {Input} from "@chakra-ui/react";
import {AddIcon, MinusIcon} from "@chakra-ui/icons";

const CartActions: FC = () => {
    const { getInputProps, getIncrementButtonProps, getDecrementButtonProps } =
        useNumberInput({
            step: 1,
            defaultValue: 1,
            min: 1
        })

    const inc = getIncrementButtonProps()
    const dec = getDecrementButtonProps()
    const input = getInputProps()

    return(
        <div>
            <HStack>
                <Button {...dec} boxSize={10}>
                    <MinusIcon width='8px'/>
                </Button>

                <Input {...input}
                       focusBorderColor='pink.400'
                       textAlign='center'
                       height='40px'
                       readOnly
                       _hover={{cursor: 'default'}}
                />

                <Button {...inc} boxSize={10}>
                    <AddIcon width='8px'/>
                </Button>
            </HStack>
        </div>

    )
}

export default CartActions