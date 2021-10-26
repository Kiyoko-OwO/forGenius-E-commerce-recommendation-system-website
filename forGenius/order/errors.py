class CartProductError(Exception):
    code = 400
    message = "This product does not exist in the cart"