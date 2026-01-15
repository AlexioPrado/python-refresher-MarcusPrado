def calculate_discount(price, is_member):
    """
    Returns the discounted price.
    Members receive a 10% discount.
    """
    if is_member:
        return price - 0.10
    return price
