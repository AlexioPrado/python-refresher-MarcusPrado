def is_even(number):
    #Error Handling: Check number data type to compute
    if not isinstance(number, int) and not isinstance(number, float):
        return "Number is not an integer or float. Input correct data type"

    #Original Line: return number % 2 == 1
    return number % 2 == 0

#Test
#print(is_even(20))
#print(is_even(67))
#print(is_even('notnumber'))