from project.models.product import Product


def get_ordered_products_by_price(products: list[Product]):
    return sorted(products, key=lambda product: product.price, reverse=True)
