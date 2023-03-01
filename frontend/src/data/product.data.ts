import {IProduct} from "../types/product.interface";

//my fake products
export const products: IProduct[] = [
    {
        id: 1,
        description: 'MacBook Pro с суперсилой M2 Pro работает без подзарядки весь день, имеет ' +
                     'превосходный дисплей Liquid Retina XDR и все необходимые порты',
        name: 'Apple MacBook Pro 16',
        images:[
            '/src/assets/productsImg/product-img1.png',
            '/src/assets/productsImg/product-img2.png'
        ],
        price: 3500,
        reviews: []
    },
    {
        id: 2,
        description: 'Волшебный способ взаимодействия с вашим Iphone. Революционные фунции безопасности,' +
                     'разработанные для спасения жизней',
        name: 'Apple iPhone 14 Pro Max',
        images:[
            '/src/assets/productsImg/product-img3.png',
            '/src/assets/productsImg/product-img4.png'
        ],
        price: 2000,
        reviews: []

    },
    {
        id: 3,
        description: 'Безкомпромиссные возможности в прочном корпусе. Непревзойденная точность' +
                     'GPS даже в мегаполисе',
        name: 'Apple Watch Ultra GPS + Cellular',
        images:[
            '/src/assets/productsImg/product-img5.png',
            '/src/assets/productsImg/product-img6.png'
        ],
        price: 1000,
        reviews: []
    },
    {
        id: 4,
        description: 'Максимально эффективное активное шумоподавление, адаптивный режим прозрачности,' +
                     'атмосферное пространственное аудио',
        name: 'Apple AirPods Pro',
        images:[
            '/src/assets/productsImg/product-img7.png',
            '/src/assets/productsImg/product-img8.png'
        ],
        price: 300,
        reviews: []
    },
    {
        id: 5,
        description: 'Увеличенное время работы в режиме телефонного разговора. ' +
                     'Активация Siri с помощью голоса. ',
        name: 'Apple AirPods (2019)',
        images:[
            '/src/assets/productsImg/product-img8.png'
        ],
        price: 200,
        reviews: []
    },
]