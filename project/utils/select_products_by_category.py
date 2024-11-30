from project.models.product import Product


def select_products_by_category(products: list[Product], category: str):
    return [p for p in products if p.category == category]
