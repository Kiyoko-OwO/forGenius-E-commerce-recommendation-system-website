class EmptyCartError(Exception):
    code = 400
    message = "Cart is empty"