from project.models.product import Product


def extract_prices(products: list[Product]):
    return [p.price for p in products]
