def calculate_discount(price, is_member):
    """
    Returns the discounted price.
    Members receive a 10% discount.
    """
    #Error Handling: Check Price & is_member data type and if Price is less than or equal to 0
    if not isinstance(price, int) and not isinstance(price, float):
        return "Price is not an integer or float. Please input a number"
    if not isinstance(is_member, bool):
        return "Cannot determine if customer is a member. Please input a true/false"
    if price <= 0:
        raise ValueError("Price is less than or equal to 0")
        #return "Price is less than or equal to 0. Please input a positive number"
    
    if is_member:
        return price * 0.90
    return price

#Test
#print(calculate_discount(60, True))
#print(calculate_discount("54", False))
#print(calculate_discount(40, 67))
#print(calculate_discount(-20,True))