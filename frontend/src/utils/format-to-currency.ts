
//вывод цен
export const formatToCurrency = (price: number) => new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
}).format(price)