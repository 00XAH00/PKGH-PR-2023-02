import {FC, useState} from 'react';
import styles from './Search.module.scss'
import {Input, InputGroup, InputLeftElement} from "@chakra-ui/react";
import {SearchIcon} from "@chakra-ui/icons";

const Search: FC = () => {
    const [searchTerm, setSearchTerm] = useState('')

    return(
        <div className={styles.search}>
            <InputGroup>
                <InputLeftElement
                    pointerEvents='none'
                    children={<SearchIcon color='gray.600'/>}
                />
                <Input
                    variant='flushed'
                    type='search'
                    onChange={e => setSearchTerm(e.target.value)}
                    value={searchTerm}
                    placeholder='Search'
                    borderColor='gray.400'
                    focusBorderColor='pink.600'
                />
            </InputGroup>
        </div>
    )
}

export default Search