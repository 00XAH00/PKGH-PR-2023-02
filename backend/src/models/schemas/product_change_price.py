from pydantic import BaseModel


class ProductChangePriceSchema(BaseModel):
    product_code: str
    new_price: int
