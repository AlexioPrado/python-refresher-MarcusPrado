def withdraw(balance, amount):
    #Error Handling: Check data type of balance and amount
    if not isinstance(balance, int) and not isinstance(balance, float):
        return "Given balance is not a number. Input the right data type"
    if not isinstance(amount, int) and not isinstance(amount, float):
        return "Given withdraw amount is not a number, Input the right data type"
    
    if amount > balance:
        return balance
    return balance - amount

#Assertions
#assert withdraw(100,25) == 75
#assert withdraw(100, 120) == 100
#assert withdraw("chicken", 20) == "Given balance is not a number. Input the right data type"
#assert withdraw(67, "so skibidi") == "Given withdraw amount is not a number, Input the right data type"